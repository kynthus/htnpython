/******************************************************************************/
/**
 * @addtogroup swiglist
 * @file       swiglist.cpp
 * @brief      SWIGによるPython-C/C++の連携
 * @date       2019-12-08
 * @author     Hatano Yusuke
 */
/******************************************************************************/

// ベクタのインクルード
#include <vector>

/**
 * @brief  リストをバブルソートして返す
 * @param  list ソート対象のリスト
 * @return ソート済みリスト
 */
std::vector<int> bubble_sort(const std::vector<int> &list) {

    // 返却用のソート済みリスト
    std::vector<int> sorted_list = list;

    // 一時ベクタ長を表す型エイリアスを定義
    typedef std::vector<int>::size_type size_type;

    // バブルソートで昇順に並べ替え
    for (size_type j = sorted_list.size(); j > static_cast<size_type>(0); --j) {

        for (size_type i = static_cast<size_type>(0); i < j - 1; ++i) {

            // 現在の要素が1つ後ろの要素より大きい場合は入れ替え
            if (sorted_list[i + 1] < sorted_list[i]) {

                std::swap(sorted_list[i], sorted_list[i + 1]);

            }

        }

    }

    // 正常終了前に生のリストを解放
    return sorted_list;

}
