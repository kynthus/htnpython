/******************************************************************************/
/**
 * @addtogroup swighello
 * @file       swighello.h
 * @brief      SWIGによるPython-C/C++のヘッダ
 * @date       2019-12-08
 * @author     Hatano Yusuke
 */
/******************************************************************************/

/* 多重インクルードの防止 */
#ifndef PYTHONAPI_SWIGHELLO_H

/**
 * @brief インクルードガード用マクロ
 */
#define PYTHONAPI_SWIGHELLO_H

// ベクタのインクルード
#include <vector>

// 関数のプロトタイプ宣言
extern std::vector<int> bubble_sort(const std::vector<int> &);

#endif /* PYTHONAPI_SWIGHELLO_H */
