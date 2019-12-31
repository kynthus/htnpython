/******************************************************************************/
/**
 * @addtogroup pycpphello
 * @file       pycpphello.cpp
 * @brief      はじめてのPython/C API(C++バージョン)
 * @date       2019-12-08
 * @author     Hatano Yusuke
 */
/******************************************************************************/

/**
 * @brief Boost.Pythonを静的リンクする
 */
#define PY_SSIZE_T_CLEAN

// C++入出力ヘッダ
#include <iostream>

// Python API用のヘッダ
#include <Python.h>

// 関数のプロトタイプ宣言
PyMODINIT_FUNC PyInit_pycpphello();

/**
 * @brief ファイルスコープにするための無名名前空間
 */
namespace {

/**
 * @brief  標準出力へ「Hello, World.」を表示する
 * @return 常に「None」を返す
 */
inline PyObject *hello(PyObject *, PyObject *)
{

    // 「Hello, World.」を表示する
    std::cout << "Hello, World." << std::endl;

    // 戻り値なしの場合は「None」を返す
    Py_RETURN_NONE;

}

/**
 * @brief  メソッド情報を初期化して返す
 * @return メソッド情報
 */
inline struct PyMethodDef *pycpphello_methods_info()
{

    // 初回呼び出しかどうか(デフォルト:TRUE)
    static int is_first = 1;

    // 登録する各種メソッドの情報
    static struct PyMethodDef methods[2];

    // 初期化は初回のみ行う
    if (is_first) {

        // 終端のインデックスを計算
        size_t end = sizeof(methods) / sizeof(*methods) - 1;

        // メソッド情報を設定する
        methods[0].ml_name = "hello";
        methods[0].ml_meth = hello;
        methods[0].ml_flags = METH_NOARGS;
        methods[0].ml_doc = "Printing 「Hello, World.」";

        // 終端には0およびNULLを設定
        methods[end].ml_name = NULL;
        methods[end].ml_meth = NULL;
        methods[end].ml_flags = 0x00;
        methods[end].ml_doc = NULL;

        // 2回目以降は初期化しないようにする
        is_first = !is_first;

    }

    // メソッド情報を返す
    return methods;

}

/**
 * @brief  モジュール情報を初期化して返す
 * @return モジュール情報
 */
inline struct PyModuleDef *pycpphello_module_info()
{

    // 初回呼び出しかどうか(デフォルト:TRUE)
    static int is_first = 1;

    // 呼出元へ返すモジュール情報
    static struct PyModuleDef module;

    // 初期化は初回のみ行う
    if (is_first) {

        // モジュール名の設定やメソッド登録を行う
        module.m_name = "pycpphello";
        module.m_doc = "Python C API Test module";
        module.m_size = static_cast<Py_ssize_t>(-1);
        module.m_methods = pycpphello_methods_info();

        // 2回目以降は初期化しないようにする
        is_first = !is_first;

    }

    // モジュール情報を返す
    return &module;

}

}

/**
 * @brief  Pythonモジュールの初期化を行う
 * @return Pythonのモジュールオブジェクト
 */
PyMODINIT_FUNC PyInit_pycpphello()
{

    // モジュールオブジェクトを生成して返す
    return PyModule_Create(pycpphello_module_info());

}
