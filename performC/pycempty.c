/******************************************************************************/
/**
 * @addtogroup pycempty
 * @file       pycempty.c
 * @brief      Python/C APIにおけるクラス(空)
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

PyMODINIT_FUNC PyInit_pycempty(void);

#else

PyMODINIT_FUNC PyInit_pycempty();

#endif

/* C++互換宣言の終わり */
#if defined(__cplusplus) || defined(c_plusplus)
}
#endif

/**
 * @brief 一切の属性もメソッドも持たない構造体
 */
struct my_empty {

    /* Python互換用の基本メンバ */
    PyObject_HEAD

};

/**
 * @brief  データ型情報を初期化して返す
 * @return データ型情報
 */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
static PyTypeObject *my_empty_type_info(void)
#else
static PyTypeObject *my_empty_type_info()
#endif
{

    /* 初回呼び出しかどうか(デフォルト:TRUE) */
    static int is_first = 1;

    /* モジュール情報を定義し、メソッドを登録 */
    static PyTypeObject type_obj;

    /* 初期化は初回のみ行う */
    if (is_first) {

        /* データ型として空のクラスの情報を設定 */
        type_obj.tp_name = "pycempty.MyEmpty";
        type_obj.tp_doc = "My empty object.";
        type_obj.tp_basicsize = (Py_ssize_t)sizeof(struct my_empty);
        type_obj.tp_itemsize = (Py_ssize_t)0;
        type_obj.tp_flags = Py_TPFLAGS_DEFAULT;
        type_obj.tp_new = PyType_GenericNew;

        /* 2回目以降は初期化しないようにする */
        is_first = !is_first;

    }

    /* データ型情報を返す */
    return (&type_obj);

}

/**
 * @brief  モジュール情報を初期化して返す
 * @return モジュール情報
 */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
static struct PyModuleDef *pycempty_module_info(void)
#else
static struct PyModuleDef *pycempty_module_info()
#endif
{

    /* 初回呼び出しかどうか(デフォルト:TRUE) */
    static int is_first = 1;

    /* 呼出元へ返すモジュール情報 */
    static struct PyModuleDef module;

    /* 初期化は初回のみ行う */
    if (is_first) {

        /* モジュール名の設定を行う(メソッドは存在しないためNULL) */
        module.m_name = "pycempty";
        module.m_doc = "Python C API Test module";
        module.m_size = (Py_ssize_t)-1;
        module.m_methods = NULL;

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
PyMODINIT_FUNC PyInit_pycempty(void)
#else
PyMODINIT_FUNC PyInit_pycempty()
#endif
{

    /* モジュールとデータ型情報 */
    PyObject *module_info;
    PyTypeObject *type_info;

    /*
     * モジュールオブジェクトを生成して返す
     * 所有参照だが、オブジェクト追加時に盗まれるため手動解放は不要
     * エラー発生時は手動で解放する
     */
    module_info = PyModule_Create(pycempty_module_info());

    /* モジュールオブジェクトの生成に失敗した場合はエラー */
    if (!module_info) {

        /* NULLリターンへ */
        goto RETURN_NULL;

    }

    /*
     * 空クラスの情報を取得
     * 正常時には参照カウントを増やし、その際は手動で減らす必要がある
     * エラー発生時は参照カウントを減らしてはならない
     */
    type_info = my_empty_type_info();

    /* データ型情報をファイナライズ */
    if (PyType_Ready(type_info)) {

        /* モジュール情報の解放処理へ */
        goto MODULE_INFO_DEF;

    }

    /* オブジェクトの追加のために参照カウントを増やす */
    Py_INCREF(type_info);

    /* モジュール情報へオブジェクトを追加 */
    if (PyModule_AddObject(module_info, "MyEmpty", (PyObject *)type_info)) {

        /* 空クラスの情報を解放する処理へ */
        goto TYPE_INFO_DEC;

    }

    /* モジュール情報を返す */
    return (module_info);

    /* 空クラスの情報を解放 */
    TYPE_INFO_DEC:
    Py_DECREF(type_info);

    /* モジュール情報を解放 */
    MODULE_INFO_DEF:
    Py_DECREF(module_info);

    /* 関数エラーリターン */
    RETURN_NULL:
    return (NULL);

}
