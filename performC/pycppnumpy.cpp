/******************************************************************************/
/**
 * @addtogroup pycppnumpy
 * @file       pycppnumpy.cpp
 * @brief      はじめてのBoost.NumPy
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

// Boost.NumPy用のヘッダ
#include <boost/python/numpy.hpp>

/**
 * @brief ファイルスコープにするための無名名前空間
 */
namespace {

/**
 * @brief  一次元のNumPy配列に対してスカラ値を乗算する
 * @param  array  乗算対象のNumPy配列
 * @param  scalar 乗算するスカラ値
 * @return 関数の実行結果
 * @retval スカラ値を乗算したNumPy配列 全要素への乗算に成功した場合
 * @retval NULL                        失敗した場合
 */
inline boost::python::numpy::ndarray mult_array(
    const boost::python::numpy::ndarray &array,
    double scalar
) {

    // 元配列の次元数・長さ・データ型を取得
    int nd = array.get_nd();
    const Py_intptr_t *shepe = array.get_shape();
    boost::python::numpy::dtype dtype = array.get_dtype();

    // 元配列と同じ次元数・長さ・データ型の返却用配列を生成
    boost::python::numpy::ndarray multed_array =
        boost::python::numpy::empty(nd, shepe, dtype);

    // 一次元目のバッファ長を取得
    Py_intptr_t length = array.shape(0);

    // 配列の各要素にスカラ値を乗算した結果を返却用配列へ設定
    for (Py_intptr_t i = static_cast<Py_intptr_t>(0); i < length; ++i) {

        // 各要素の値を格納する変数
        double element;

        // 要素をdouble型として変数へコピー
        (void)memcpy(
            &element,
            array.get_data() + array.get_dtype().get_itemsize() * i,
            sizeof(element)
        );

        // 要素にスカラ値を乗算した値を返却用配列へコピー
        multed_array[i] = element * scalar;

    }

    // 乗算後の配列を返す
    return multed_array;

}

}

/**
 * @brief mult_array関数をPython用として登録するマクロ関数
 */
BOOST_PYTHON_MODULE(pycppnumpy) {

    // はじめにBoost.NumPyを初期化
    // これを忘れるとSIGSEGVでダウンする
    boost::python::numpy::initialize();

    // NumPy配列の乗算関数を登録
    boost::python::def(
        "mult_array",
        mult_array,
        boost::python::args("array", "scalar"),
        "NumPy's array multiplier."
    );

}
