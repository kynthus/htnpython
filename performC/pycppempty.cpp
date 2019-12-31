/******************************************************************************/
/**
 * @addtogroup pycppempty
 * @file       pycppempty.cpp
 * @brief      Boost.Pythonにおけるクラス(空)
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
 * @brief 一切の属性もメソッドも持たないクラスを表現
 */
class MyEmpty {};

}

/**
 * @brief 空のクラスをPython用に登録する
 */
BOOST_PYTHON_MODULE(pycppempty) {

    // MyEmptyクラスを登録
    boost::python::class_<MyEmpty>("MyEmpty");

}
