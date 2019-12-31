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

/* C++互換宣言の始まり */
#if defined(__cplusplus) || defined(c_plusplus)
extern "C" {
#endif

/* 関数のプロトタイプ宣言 */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)

extern int hello(const char *);

#else

extern int hello();

#endif

/* C++互換宣言の終わり */
#if defined(__cplusplus) || defined(c_plusplus)
}
#endif

#endif /* PYTHONAPI_SWIGHELLO_H */
