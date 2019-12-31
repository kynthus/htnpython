/******************************************************************************/
/**
 * @addtogroup pycpplist
 * @file       pycpplist.cpp
 * @brief      はじめてのPython/C API(Boost.Pythonバージョン)
 * @date       2019-12-08
 * @author     Hatano Yusuke
 */
/******************************************************************************/

/**
 * @brief Boost.Pythonを静的リンクする
 */
#define BOOST_PYTHON_STATIC_LIB

// C++入出力ヘッダ
#include <vector>

// Boost.Python用のヘッダ
#include <boost/python.hpp>

/**
 * @brief ファイルスコープにするための無名名前空間
 */
namespace {

/**
 * @brief  リストをバブルソートして返す
 * @param  list ソート対象のリスト
 * @return ソート済みリスト
 */
inline boost::python::list bubble_sort(const boost::python::list &list) {

    // バブルソート時に用いる一時ベクタ
    std::vector<int> raw_list = std::vector<int>(
        boost::python::stl_input_iterator<int>(list),
        boost::python::stl_input_iterator<int>()
    );

    // 一時ベクタ長を表す型エイリアスを定義
    typedef std::vector<int>::size_type size_type;

    // バブルソートで昇順に並べ替え
    for (size_type j = raw_list.size(); j > static_cast<size_type>(0); --j) {

        for (size_type i = static_cast<size_type>(0); i < j - 1; ++i) {

            // 現在の要素が1つ後ろの要素より大きい場合は入れ替え
            if (raw_list[i + 1] < raw_list[i]) {

                std::swap(raw_list[i], raw_list[i + 1]);

            }

        }

    }

    // 返却用のソート済みリスト
    boost::python::list sorted_list;

    // 一時ベクタのイテレータを表す型エイリアスを定義
    typedef std::vector<int>::const_iterator const_iterator;

    // 一時配列の全要素を返却用リストへコピーする
    for (const_iterator iter = raw_list.begin(); iter != raw_list.end(); ++iter) {

        sorted_list.append(*iter);

    }

    // 正常終了前に生のリストを解放
    return sorted_list;

}

}

/**
 * @brief bubble_sort関数をPython用として登録するマクロ関数
 */
BOOST_PYTHON_MODULE(pycpplist) {

    // helloをPythonの関数として登録
    boost::python::def("bubble_sort", bubble_sort);

}
