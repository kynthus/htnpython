/******************************************************************************/
/**
 * @addtogroup pychello
 * @file       pychello.c
 * @brief      はじめてのPython/C API
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

/* C++互換宣言の始まり */
#if defined(__cplusplus) || defined(c_plusplus)
extern "C" {
#endif

/* 関数のプロトタイプ宣言 */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)

PyMODINIT_FUNC PyInit_pychello(void);

#else

PyMODINIT_FUNC PyInit_pychello();

#endif

/* C++互換宣言の終わり */
#if defined(__cplusplus) || defined(c_plusplus)
}
#endif

/**
 * @brief  標準出力へ「Hello, World.」を表示する
 * @param  self 関数・メソッドのレシーバ(未使用)
 * @param  args 関数・メソッドの引数(未使用)
 * @return 常に「None」を返す
 */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
static PyObject *hello(PyObject *self, PyObject *args)
#else
static PyObject *hello(self, args)
PyObject *self;
PyObject *args;
#endif
{

    /* 引数未使用警告の抑止 */
    (void)self;
    (void)args;

    /* 「Hello, World.」を表示する */
    (void)puts("Hello, World.");

    /* 戻り値なしの場合は「None」を返す */
    Py_RETURN_NONE;

}

/**
 * @brief  メソッド情報を初期化して返す
 * @return メソッド情報
 */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
static struct PyMethodDef *pychello_methods_info(void)
#else
static struct PyMethodDef *pychello_methods_info()
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
        methods[0].ml_name = "hello";
        methods[0].ml_meth = hello;
        methods[0].ml_flags = METH_NOARGS;
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
static struct PyModuleDef *pychello_module_info(void)
#else
static struct PyModuleDef *pychello_module_info()
#endif
{

    /* 初回呼び出しかどうか(デフォルト:TRUE) */
    static int is_first = 1;

    /* 呼出元へ返すモジュール情報 */
    static struct PyModuleDef module;

    /* 初期化は初回のみ行う */
    if (is_first) {

        /* モジュール名の設定やメソッド登録を行う */
        module.m_name = "pychello";
        module.m_doc = "Python C API Test module";
        module.m_size = (Py_ssize_t)-1;
        module.m_methods = pychello_methods_info();

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
PyMODINIT_FUNC PyInit_pychello(void)
#else
PyMODINIT_FUNC PyInit_pychello()
#endif
{

    /* モジュールオブジェクトを生成して返す */
    return (PyModule_Create(pychello_module_info()));

}
