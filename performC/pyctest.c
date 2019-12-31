/******************************************************************************/
/**
 * @addtogroup pyctest
 * @file       pyctest.c
 * @brief      Python/C APIのテストモジュール
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

PyMODINIT_FUNC PyInit_pyctest(void);

#else

PyMODINIT_FUNC PyInit_pyctest();

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
static PyObject *prog01_01(PyObject *self, PyObject *args)
#else
static PyObject *prog01_01(self, args)
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
 * @brief  CからPythonの関数を呼び出す
 * @param  self 関数・メソッドのレシーバ(未使用)
 * @param  args 関数・メソッドの引数(未使用)
 * @return 関数の実行結果
 * @retval Py_None 正常終了
 * @retval NULL    異常終了
 */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
static PyObject *prog01_02(PyObject *self, PyObject *args)
#else
static PyObject *prog01_02(self, args)
PyObject *self;
PyObject *args;
#endif
{

    /* モジュールと関数の情報 */
    PyObject *module_info;
    PyObject *func_info;

    /* Pythonのprint関数へ渡す引数 */
    PyObject *arg_tuple;
    PyObject *arg_msg;

    /* 関数呼出結果 */
    PyObject *call_result;

    /* 引数未使用警告の抑止 */
    (void)self;
    (void)args;

    /*
     * 「builtins」モジュールをインポートし、その結果を受け取る
     * 借用参照のため手動解放してはならない
     */
    module_info = PyEval_GetBuiltins();

    /* インポートが失敗した場合はエラー */
    if (!module_info) {

        /* NULLリターンへ */
        goto RETURN_NULL;

    }

    /*
     * print関数の情報を取得する
     * 所有参照のため手動解放が必要
     */
    func_info = PyMapping_GetItemString(module_info, "print");

    /* 情報取得に失敗した場合はエラー */
    if (!func_info) {

        /* NULLリターンへ */
        goto RETURN_NULL;

    }

    /*
     * print関数の引数とする文字列を格納するタプル(長さは1)
     * 所有参照のため手動解放が必要
     */
    arg_tuple = PyTuple_New((Py_ssize_t)1);

    /* タプルの生成に失敗した場合はエラー */
    if (!arg_tuple) {

        /* 引数格納用タプルの解放処理へ */
        goto FUNC_INFO_DEC;

    }

    /*
     * 表示するメッセージをPythonのUnicode文字列として生成
     * 所有参照だが、タプルへの格納時に盗まれるため手動解放は不要
     * エラー発生時は手動で解放する
     */
    arg_msg = PyUnicode_FromString("Hello, World with Python's print().");

    /* 表示メッセージの生成に失敗した場合はエラー */
    if (!arg_msg) {

        /* 引数格納用タプルの解放処理へ */
        goto ARG_TUPLE_DEC;

    }

    /* タプルへの設定に失敗した場合はエラー */
    if (PyTuple_SetItem(arg_tuple, (Py_ssize_t)0, arg_msg)) {

        /* 表示メッセージの解放処理へ */
        goto ARG_MSG_DEC;

    }

    /*
     * Pythonのprint関数を呼び出す
     * 所有参照のため手動解放が必要
     */
    call_result = PyObject_CallObject(func_info, arg_tuple);

    /* 関数呼出に失敗した場合はエラー */
    if (!call_result) {

        /* 引数格納用タプルの解放処理へ */
        goto ARG_TUPLE_DEC;

    }

    /* 正常リターン前に手動解放する */
    Py_DECREF(func_info);
    Py_DECREF(arg_tuple);
    Py_DECREF(call_result);

    /* 「None」を返して正常リターン */
    Py_RETURN_NONE;

    /* 表示文字列の解放 */
    ARG_MSG_DEC:
    Py_DECREF(arg_msg);

    /* 引数格納用タプルの解放 */
    ARG_TUPLE_DEC:
    Py_DECREF(arg_tuple);

    /* print関数情報の解放 */
    FUNC_INFO_DEC:
    Py_DECREF(func_info);

    /* 関数エラーリターン */
    RETURN_NULL:
    return (NULL);

}

/**
 * @brief  Pythonの整数型変数を扱う
 * @param  self 関数・メソッドのレシーバ(未使用)
 * @param  args 関数・メソッドの引数(未使用)
 * @return 関数の実行結果
 * @retval Py_None 正常終了
 * @retval NULL    異常終了
 */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
static PyObject *prog01_03(PyObject *self, PyObject *args)
#else
static PyObject *prog01_03(self, args)
PyObject *self;
PyObject *args;
#endif
{

    /* Pythonの整数型と、それに対応するC言語のlong型 */
    PyObject *pyvar;
    long cvar;

    /* エラー判定用の問い合わせ結果 */
    PyObject *is_error;

    /* 引数未使用警告の抑止 */
    (void)self;
    (void)args;

    /*
     * Pythonの整数型をPyObjectとして生成
     * 所有参照のため手動解放が必要
     */
    pyvar = PyLong_FromLong(100L);

    /* 変数の生成に失敗した場合はエラー */
    if (!pyvar) {

        /* 関数エラーリターン */
        return (NULL);

    }

    /* Pythonの整数型をC言語のlong型へ変換 */
    cvar = PyLong_AsLong(pyvar);

    /*
     * いったんエラー判定を行ってからPythonの変数を解放
     * 借用参照のため手動解放してはならない
     */
    is_error = PyErr_Occurred();
    Py_DECREF(pyvar);

    /* long型への変換に失敗した場合はエラー */
    if (is_error) {

        /* 関数エラーリターン */
        return (NULL);

    }

    /* 取得した整数値をprintf()で表示 */
    (void)printf("num is %ld\n", cvar);

    /* 「None」を返して正常リターン */
    Py_RETURN_NONE;

}

/**
 * @brief  2つの引数を加算する
 * @param  self 関数・メソッドのレシーバ(未使用)
 * @param  args 加算対象の整数値(引数を2個使用)
 * @return 関数の実行結果
 * @retval 加算後の整数 加算に成功した場合
 * @retval NULL         加算に失敗した場合
 */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
static PyObject *prog01_04(PyObject *self, PyObject *args)
#else
static PyObject *prog01_04(self, args)
PyObject *self;
PyObject *args;
#endif
{

    /* 足される数と足す数 */
    int augend;
    int addend;

    /* 引数未使用警告の抑止 */
    (void)self;

    /* 引数のタプルを解析する */
    if (!PyArg_ParseTuple(args, "ii", &augend, &addend)) {

        /* 関数エラーリターン */
        return (NULL);

    }

    /* 加算結果を返す */
    return (PyLong_FromLong((long)augend + addend));

}

/**
 * @brief  2つの引数を加算する(キーワード付き引数版)
 * @param  self   関数・メソッドのレシーバ(未使用)
 * @param  args   加算対象の整数値(引数を2個使用)
 * @param  kwargs キーワード付き引数(未使用)
 * @return 関数の実行結果
 * @retval 加算後の整数 加算に成功した場合
 * @retval NULL         加算に失敗した場合
 */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
static PyObject *prog01_05(PyObject *self, PyObject *args, PyObject *kwargs)
#else
static PyObject *prog01_05(self, args, kwargs)
PyObject *self;
PyObject *args;
PyObject *kwargs;
#endif
{

    /* 足される数と足す数 */
    int augend;
    int addend;

    /* それぞれのキーワード名 */
    static char augend_key[] = "augend";
    static char addend_key[] = "addend";

    /* キーワード文字列を指定する */
    static char *keywords[] = {augend_key, addend_key, NULL};

    /* 引数未使用警告の抑止 */
    (void)self;
    (void)kwargs;

    /* 引数のタプルを解析する */
    if (!PyArg_ParseTupleAndKeywords(args, kwargs, "ii", keywords, &augend, &addend)) {

        /* 関数エラーリターン */
        return (NULL);

    }

    /* 加算結果を返す */
    return (PyLong_FromLong((long)augend + addend));

}

/**
 * @brief  メソッド情報を初期化して返す
 * @return メソッド情報
 */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
static struct PyMethodDef *my_test_methods_info(void)
#else
static struct PyMethodDef *my_test_methods_info()
#endif
{

    /* 初回呼び出しかどうか(デフォルト:TRUE) */
    static int is_first = 1;

    /* 登録する各種メソッドの情報 */
    static struct PyMethodDef methods[6];

    /* 初期化は初回のみ行う */
    if (is_first) {

        /* 終端のインデックスを計算 */
        size_t end = sizeof(methods) / sizeof(*methods) - 1;

        /* メソッド情報を設定する */
        methods[0].ml_name = "prog01_01";
        methods[0].ml_meth = prog01_01;
        methods[0].ml_flags = METH_NOARGS;
        methods[0].ml_doc = "Printing 「Hello, World.」";

        methods[1].ml_name = "prog01_02";
        methods[1].ml_meth = prog01_02;
        methods[1].ml_flags = METH_NOARGS;
        methods[1].ml_doc = "Printing 「Hello, World.」 with Python func.";

        methods[2].ml_name = "prog01_03";
        methods[2].ml_meth = prog01_03;
        methods[2].ml_flags = METH_NOARGS;
        methods[2].ml_doc = "Generating integer variable.";

        methods[3].ml_name = "prog01_04";
        methods[3].ml_meth = prog01_04;
        methods[3].ml_flags = METH_VARARGS;
        methods[3].ml_doc = "Add 2 integers.";

        methods[4].ml_name = "prog01_05";
        methods[4].ml_meth = (PyCFunction)prog01_05;
        methods[4].ml_flags = METH_VARARGS | METH_KEYWORDS;
        methods[4].ml_doc = "Add 2 integers with keyword.";

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
static struct PyModuleDef *my_test_module_info(void)
#else
static struct PyModuleDef *my_test_module_info()
#endif
{

    /* 初回呼び出しかどうか(デフォルト:TRUE) */
    static int is_first = 1;

    /* 呼出元へ返すモジュール情報 */
    static struct PyModuleDef module;

    /* 初期化は初回のみ行う */
    if (is_first) {

        /* モジュール名の設定やメソッド登録を行う */
        module.m_name = "pyctest";
        module.m_doc = "Python C API Test module";
        module.m_size = (Py_ssize_t)-1;
        module.m_methods = my_test_methods_info();

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
PyMODINIT_FUNC PyInit_pyctest(void)
#else
PyMODINIT_FUNC PyInit_pyctest()
#endif
{

    /* モジュールオブジェクトを生成して返す */
    return (PyModule_Create(my_test_module_info()));

}
