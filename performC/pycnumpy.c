/******************************************************************************/
/**
 * @addtogroup pycnumpy
 * @file       pycnumpy.c
 * @brief      はじめてのNumPy/C API
 * @date       2019-12-08
 * @author     Hatano Yusuke
 */
/******************************************************************************/

/**
 * @brief サイズ値をintではなく、ssize_tで扱うためのマクロ
 */
#define PY_SSIZE_T_CLEAN

/* Python API用のヘッダ */
#include <Python.h>

/* NumPy用のヘッダ */
#include <numpy/arrayobject.h>
#include <numpy/arrayscalars.h>

/* C++互換宣言の始まり */
#if defined(__cplusplus) || defined(c_plusplus)
extern "C" {
#endif

/* 関数のプロトタイプ宣言 */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)

PyMODINIT_FUNC PyInit_pycnumpy(void);

#else

PyMODINIT_FUNC PyInit_pycnumpy();

#endif

/* C++互換宣言の終わり */
#if defined(__cplusplus) || defined(c_plusplus)
}
#endif

/**
 * @brief  一次元のNumPy配列に対してスカラ値を乗算する
 * @param  self   関数・メソッドのレシーバ(未使用)
 * @param  args   可変引数
 * @param  kwargs キーワード付き引数
 * @return 関数の実行結果
 * @retval スカラ値を乗算したNumPy配列 全要素への乗算に成功した場合
 * @retval NULL                        失敗した場合
 */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
static PyObject *mult_array(PyObject *self, PyObject *args, PyObject *kwargs)
#else
static PyObject *mult_array(self, args, kwargs)
PyObject *self;
PyObject *args;
PyObject *kwargs;
#endif
{

    /* 足される数と足す数 */
    PyArrayObject *array;
    double scalar;

    /* 元配列の次元数・長さ・データ型 */
    int nd;
    npy_intp *dims;
    PyArray_Descr *dtype;

    /* 返却用のNumPy配列 */
    PyArrayObject *multed_array;

    /* 入力元NumPy配列のバッファ長とカウンタ */
    npy_intp length;
    npy_intp i;

    /* それぞれのキーワード名 */
    static char array_key[] = "array";
    static char scalar_key[] = "scalar";

    /* キーワード文字列を指定する */
    static char *keywords[] = {array_key, scalar_key, NULL};

    /* 引数未使用警告の抑止 */
    (void)self;

    /* 引数のタプルを解析する */
    if (!PyArg_ParseTupleAndKeywords(
        args, kwargs,
        "O!d", keywords,
        &PyArray_Type, &array,
        &scalar
    )) {

        /* 関数エラーリターン */
        return (NULL);

    }

    /* パースした引数を使用するため、参照カウントを増やす */
    Py_INCREF(array);

    /* 元配列の次元数・長さ・データ型を取得 */
    nd = array->nd;
    dims = array->dimensions;
    dtype = array->descr;

    /* 元配列と同じ次元数・長さ・データ型の返却用配列を生成 */
    multed_array = (PyArrayObject *)PyArray_Empty(nd, dims, dtype, 0);

    /* 返却用配列の生成に失敗した場合はエラー */
    if (!multed_array) {

        /* 関数エラーリターン */
        return (NULL);

    }

    /* 一次元目のバッファ長を取得 */
    length = *array->dimensions;

    /* 配列の各要素に対し、スカラ値を乗算した結果を返却用配列へ設定 */
    for (i = (npy_intp)0; i < length; i++) {

        /* 各要素の値を格納する変数 */
        double element;

        /* 要素をdouble型として変数へコピー */
        (void)memcpy(
            &element,
            array->data + array->descr->elsize * i,
            sizeof(element)
        );

        /* 要素にスカラ値を乗算する */
        element *= scalar;

        /* 乗算した値を返却用配列へコピー */
        (void)memcpy(
            multed_array->data + multed_array->descr->elsize * i,
            &element,
            (size_t)multed_array->descr->elsize
        );

    }

    /* 乗算後の配列を返す */
    return ((PyObject *)multed_array);

}

/**
 * @brief  メソッド情報を初期化して返す
 * @return メソッド情報
 */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
static struct PyMethodDef *pycnumpy_methods_info(void)
#else
static struct PyMethodDef *pycnumpy_methods_info()
#endif
{

    /* 初回呼び出しかどうか(デフォルト:TRUE) */
    static int is_first = 1;

    /* 登録する各種メソッドの情報 */
    static struct PyMethodDef methods[2];

    /* 初期化は初回のみ行う */
    if (is_first) {

        /* 終端のインデックスを計算 */
        size_t end = sizeof(methods) / sizeof(*methods) - 1;

        /* メソッド情報を設定する */
        methods[0].ml_name = "mult_array";
        methods[0].ml_meth = (PyCFunction)mult_array;
        methods[0].ml_flags = METH_VARARGS | METH_KEYWORDS;
        methods[0].ml_doc = "Printing 「Hello, World.」";

        /* 終端には0およびNULLを設定 */
        methods[end].ml_name = NULL;
        methods[end].ml_meth = NULL;
        methods[end].ml_flags = 0x00;
        methods[end].ml_doc = NULL;

        /* 2回目以降は初期化しないようにする */
        is_first = !is_first;

    }

    /* メソッド情報を返す */
    return (methods);

}

/**
 * @brief  モジュール情報を初期化して返す
 * @return モジュール情報
 */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
static struct PyModuleDef *pycnumpy_module_info(void)
#else
static struct PyModuleDef *pycnumpy_module_info()
#endif
{

    /* 初回呼び出しかどうか(デフォルト:TRUE) */
    static int is_first = 1;

    /* 呼出元へ返すモジュール情報 */
    static struct PyModuleDef module;

    /* 初期化は初回のみ行う */
    if (is_first) {

        /* モジュール名の設定やメソッド登録を行う */
        module.m_name = "pycnumpy";
        module.m_doc = "Python C API Test module";
        module.m_size = (Py_ssize_t)-1;
        module.m_methods = pycnumpy_methods_info();

        /* 2回目以降は初期化しないようにする */
        is_first = !is_first;

    }

    /* モジュール情報を返す */
    return (&module);

}

/**
 * @brief  Pythonモジュールの初期化を行う
 * @return Pythonのモジュールオブジェクト
 */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
PyMODINIT_FUNC PyInit_pycnumpy(void)
#else
PyMODINIT_FUNC PyInit_pycnumpy()
#endif
{

    /*
     * はじめにNumPyのAPIを初期化
     * これを忘れるとSIGSEGVでダウンする
     */
    import_array();

    /* モジュールオブジェクトを生成して返す */
    return (PyModule_Create(pycnumpy_module_info()));

}
