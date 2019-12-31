/******************************************************************************/
/**
 * @addtogroup pycpptest
 * @file       pycpptest.cpp
 * @brief      Boost.Pythonのテストモジュール
 * @date       2019-12-08
 * @author     Hatano Yusuke
 */
/******************************************************************************/

/**
 * @brief Boost.Pythonを静的リンクする
 */
#define BOOST_PYTHON_STATIC_LIB

// C++入出力ヘッダ
#include <iostream>

// Boost.Python用のヘッダ
#include <boost/python.hpp>

/**
 * @brief ファイルスコープにするための無名名前空間
 */
namespace {

/**
 * @brief 標準出力へ「Hello, World.」を表示する
 */
inline void prog01_01() {

    // 「Hello, World.」を表示する
    std::cout << "Hello, World." << std::endl;

}

/**
 * @brief Boostを用いてPythonの関数を呼び出す
 */
inline void prog01_02() {

    // 「Hello, World.」を表示する
    boost::python::exec("print('Hello, World with Boost.Python print().')");

}

/**
 * @brief 変数を使う
 */
inline void prog01_03() {

    // 変数へ100を代入しておく
    int cvar = 100;

    // 「Hello, World.」を表示する
    std::cout << "num is " << cvar << std::endl;

}

/**
 * @brief  2つの引数を加算する
 * @param  augend 被加数
 * @param  addend 加数
 * @return 引数を加算した結果
 */
inline int prog01_04(int augend, int addend) {

    // 変数へ100を代入しておく
    return augend + addend;

}

/**
 * @brief  2つの引数を加算する(キーワード付き引数版)
 * @param  augend 被加数
 * @param  addend 加数
 * @return 引数を加算した結果
 */
inline int prog01_05(int augend, int addend) {

    // 変数へ100を代入しておく
    return augend + addend;

}

}

/**
 * @brief  2つの引数を加算する
 * @param  augend 被加数
 * @param  addend 加数
 * @return 引数を加算した結果
 */
BOOST_PYTHON_MODULE(pycpptest) {

    // 計5つ分登録
    boost::python::def(
        "prog01_01",
        prog01_01,
        "Printing 「Hello, World.」"
    );

    boost::python::def(
        "prog01_02",
        prog01_02,
        "Printing 「Hello, World.」 with Python func."
    );

    boost::python::def(
        "prog01_03",
        prog01_03,
        "Generating integer variable."
    );

    boost::python::def(
        "prog01_04",
        prog01_04,
        "Add 2 integers."
    );

    boost::python::def(
        "prog01_05",
        prog01_05,
        boost::python::args("augend", "addend"),
        "Add 2 integers with keyword."
    );

}
