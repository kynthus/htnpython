/******************************************************************************/
/**
 * @addtogroup pycppboost
 * @file       pycppboost.cpp
 * @brief      はじめてのBoost.Python
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
inline void hello() {

    // 「Hello, World.」を表示する
    std::cout << "Hello, World!!!" << std::endl;

}

}

/**
 * @brief hello関数をPython用として登録するマクロ関数
 */
BOOST_PYTHON_MODULE(pycppboost) {

    // helloをPythonの関数として登録
    boost::python::def("hello", hello);

}
