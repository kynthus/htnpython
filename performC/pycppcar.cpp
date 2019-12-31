/******************************************************************************/
/**
 * @addtogroup pycppcar
 * @file       pycppcar.cpp
 * @brief      Boost.Pythonにおけるクラス(属性とメソッド持ち)
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
 * @brief わたしの車クラス
 */
class MyCar {

    // メンバ変数の定義
    public:

    /**
     * @brief 車種
     */
    std::string name;

    /**
     * @brief 走行距離
     */
    double mileage;

    /**
     * @brief 値段
     */
    int price;

    // コンストラクタの定義
    public:

    /**
     * @brief 引数をもとに車クラスを初期化する
     * @param n 車種
     * @param m 走行距離
     * @param p 価格
     */
    inline MyCar(const std::string &n, double m, int p):
    name(n), mileage(m), price(p) {}

    // メソッドの定義
    public:

    /**
     * @brief 車の情報を表示する
     */
    void introduction() const {

        // 車情報を表示する
        std::cout <<
            "My car's information [" <<
            "name: " << this->name << ", " <<
            "mileage: " << this->mileage << ", " <<
            "price: " << this->price << ']' <<
            std::endl;

    }

};

}

/**
 * @brief 車クラスをPython用に登録する
 */
BOOST_PYTHON_MODULE(pycppcar) {

    // MyCarクラスを登録
    boost::python::class_<MyCar>(
        "MyCar",
        boost::python::init<const std::string &, double, int>()
    ).def_readwrite(
        "name",
        &MyCar::name
    ).def_readwrite(
        "mileage",
        &MyCar::mileage
    ).def_readwrite(
        "price",
        &MyCar::price
    ).def(
        "introduction",
        &MyCar::introduction
    );

}
