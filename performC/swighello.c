/******************************************************************************/
/**
 * @addtogroup swighello
 * @file       swighello.c
 * @brief      SWIGによるPython-C/C++の連携
 * @date       2019-12-08
 * @author     Hatano Yusuke
 */
/******************************************************************************/

/* 標準入出力ヘッダ */
#include <stdio.h>

/**
 * @brief  標準出力へ文字列を表示する
 * @param  message 表示する文字列
 * @return 関数の実行結果
 * @retval 0   正常に表示が完了した場合
 * @retval 非0 エラーが発生した場合
 */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
int hello(const char *message)
#else
int hello(message)
char *message;
#endif
{

    /* 表示文字列がNULLの場合はエラー */
    if (!message) {

        /* エラーリターンを示す-1を返す */
        return (-1);

    }

    /*
     * 文字列を標準出力へ表示する
     * 戻り値がEOFの場合はエラー扱い
     */
    if (puts(message) == EOF) {

        /* エラーリターンを示す-1を返す */
        return (-1);

    }

    /* 正常リターンを示す0を返す */
    return (0);

}
