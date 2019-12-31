/******************************************************************************/
/**
 * @addtogroup pyclist
 * @file       pyclist.c
 * @brief      PythonのリストをCから使う
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

PyMODINIT_FUNC PyInit_pyclist(void);

#else

PyMODINIT_FUNC PyInit_pyclist();

#endif

/* C++互換宣言の終わり */
#if defined(__cplusplus) || defined(c_plusplus)
}
#endif

/**
 * @brief  リストをバブルソートして返す
 * @param  self 関数・メソッドのレシーバ(未使用)
 * @param  args ソート対象のリスト
 * @return 関数の実行結果
 * @retval ソート済みリスト ソート成功時
 * @retval NULL             ソート失敗時
 */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
static PyObject *bubble_sort(PyObject *self, PyObject *args)
#else
static PyObject *bubble_sort(self, args)
PyObject *self;
PyObject *args;
#endif
{

    /* Pythonのリスト用APIで使用する変数 */
    PyObject *list;
    Py_ssize_t length;
    Py_ssize_t list_index;

    /* C言語用の一時配列とカウンタ */
    int *raw_list;
    size_t j;

    /* 返却用のソート済みリスト */
    PyObject *sorted_list;

    /* 引数未使用警告の抑止 */
    (void)self;

    /*
     * 引数よりPythonのリストを取得
     * 所有参照のため手動で解放が必要
     */
    list = PySequence_List(args);

    /* リストの取得に失敗した場合 */
    if (!list) {

        /* NULLリターンへ */
        goto RETURN_NULL;

    }

    /* リスト長を取得 */
    length = PyList_Size(list);

    /* リスト長が負数の場合はエラー */
    if (length < (Py_ssize_t)0) {

        /* リストの解放処理へ */
        goto LIST_DEC;

    }

    /* リスト長分のint型を格納できる一時配列を生成 */
    raw_list = (int *)malloc(sizeof(*raw_list) * (size_t)length);

    /* 一時配列の生成に失敗した場合はエラー */
    if (!raw_list) {

        /* リストの解放処理へ */
        goto LIST_DEC;

    }

    /* リストの全要素を一時配列へコピーする */
    for (list_index = (Py_ssize_t)0; list_index < length; list_index++) {

        /* リストの要素とエラー確認用の変数 */
        int num;
        PyObject *is_error;

        /*
         * リストの要素をPythonの整数型として取得
         * 借用参照のため手動解放してはならない
         */
        PyObject *item = PyList_GetItem(list, list_index);

        /* 要素取得に失敗した場合はエラー */
        if (!item) {

            /* 一時配列の解放処理へ */
            goto RAW_LIST_FREE;

        }

        /* Pythonの整数型をC言語のlong型へ変換 */
        num = (int)PyLong_AsLong(item);

        /*
         * long型への変換に失敗していないかを確認
         * 借用参照のため手動解放してはならない
         */
        is_error = PyErr_Occurred();

        /* 変換に失敗していた場合はエラー */
        if (is_error) {

            /* 一時配列の解放処理へ */
            goto RAW_LIST_FREE;

        }

        /* Pythonのリストから取得した値を一時配列へ格納 */
        raw_list[(size_t)list_index] = num;

    }

    /* 一時配列をバブルソートで昇順に並べ替え */
    for (j = (size_t)length; j > (size_t)0; j--) {

        size_t i;

        for (i = (size_t)0; i < j - 1; i++) {

            /* 現在の要素が1つ後ろの要素より大きい場合は入れ替え */
            if (raw_list[i + 1] < raw_list[i]) {

                int tmp = raw_list[i];
                raw_list[i] = raw_list[i + 1];
                raw_list[i + 1] = tmp;

            }

        }

    }

    /* 返却用リストを生成 */
    sorted_list = PyList_New(length);

    /* 返却用リストの生成に失敗した場合はエラー */
    if (!sorted_list) {

        /* 一時配列の解放処理へ */
        goto RAW_LIST_FREE;

    }

    /* 一時配列の全要素を返却用リストへコピーする */
    for (list_index = (Py_ssize_t)0; list_index < length; list_index++) {

        /*
         * C言語のlong型をPythonの整数型へ変換
         * 所有参照だが、リストへの格納時に盗まれるため手動解放は不要
         * エラー発生時は手動で解放する
         */
        PyObject *item = PyLong_FromLong((long)raw_list[(size_t)list_index]);

        /* 変換に失敗した場合はエラー */
        if (!item) {

            /* 返却用リストの解放処理へ */
            goto SORTED_LIST_DEC;

        }

        /* 一時配列の値を返却用リストへ格納 */
        if(PyList_SetItem(sorted_list, list_index, item)) {

            /* エラー発生時はPythonの整数型を手動解放 */
            Py_DECREF(item);

            /* 返却用リストの解放処理へ */
            goto SORTED_LIST_DEC;

        }

    }

    /* 正常終了前に生のリストを解放 */
    free(raw_list);

    /* ソート済みリストを返す */
    return (sorted_list);

    SORTED_LIST_DEC:
    Py_DECREF(sorted_list);

    /* 異常終了前に生のリストを解放 */
    RAW_LIST_FREE:
    free(raw_list);

    /* モジュール情報を解放 */
    LIST_DEC:
    Py_DECREF(list);

    /* 関数エラーリターン */
    RETURN_NULL:
    return (NULL);

}

/**
 * @brief  メソッド情報を初期化して返す
 * @return メソッド情報
 */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
static struct PyMethodDef *pyclist_methods_info(void)
#else
static struct PyMethodDef *pyclist_methods_info()
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
        methods[0].ml_name = "bubble_sort";
        methods[0].ml_meth = bubble_sort;
        methods[0].ml_flags = METH_O;
        methods[0].ml_doc = "Sorting list with bubble sort.";

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
static struct PyModuleDef *pyclist_module_info(void)
#else
static struct PyModuleDef *pyclist_module_info()
#endif
{

    /* 初回呼び出しかどうか(デフォルト:TRUE) */
    static int is_first = 1;

    /* 呼出元へ返すモジュール情報 */
    static struct PyModuleDef module;

    /* 初期化は初回のみ行う */
    if (is_first) {

        /* モジュール名の設定やメソッド登録を行う */
        module.m_name = "pyclist";
        module.m_doc = "Python C API list operation.";
        module.m_size = (Py_ssize_t)-1;
        module.m_methods = pyclist_methods_info();

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
PyMODINIT_FUNC PyInit_pyclist(void)
#else
PyMODINIT_FUNC PyInit_pyclist()
#endif
{

    /* モジュールオブジェクトを生成して返す */
    return (PyModule_Create(pyclist_module_info()));

}
