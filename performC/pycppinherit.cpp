/******************************************************************************/
/**
 * @addtogroup pycppinherit
 * @file       pycppinherit.cpp
 * @brief      Boost.Pythonにおける継承
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

    // 公開メンバ変数の定義
    public:

    /**
     * @brief 車種
     */
    std::string name;

    /**
     * @brief 走行距離
     */
    double mileage;

    // 非公開メンバ変数の定義
    private:

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
     * @brief  車の値段を取得する
     * @return 値段をラップしたPythonのlong型
     */
    int getPrice() const {

        // 値段を返す
        return this->price;

    }

    /**
     * @brief 車の値段を取得する
     * @param p 設定する値段
     */
    void setPrice(int p) {

        // 値段に負数は許容しない
        if (price < 0) {

            // 引数不正とする
            throw std::invalid_argument("Cannot setting negative price.");

        }

        // 値段を設定する
        this->price = p;

    }

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

    // デストラクタの定義
    public:

    /**
     * @brief 派生クラスを解放するための仮想デストラクタ
     */
    inline virtual ~MyCar() {}

};

/**
 * @brief F1カークラス
 */
class F1Car: public MyCar {

    // 公開メンバ変数の定義
    public:

    /**
     * @brief 速度
     */
    double speed;

    // コンストラクタの定義
    public:

    /**
     * @brief 引数をもとにF1カークラスを初期化する
     * @param n 車種
     * @param m 走行距離
     * @param p 価格
     * @param s 速度
     */
    inline F1Car(const std::string &n, double m, int p, double s):
    MyCar(n, m, p), speed(s) {}

    // メソッドの定義
    public:

    /**
     * @brief F1カーを走らせる
     */
    void run() const {

        // まずは車の紹介
        this->introduction();

        // F1カーを走らす
        std::cout << "3, 2, 1, Go!!! speed[" << this->speed << "(km)]" << std::endl;

    }

};

}

/**
 * @brief 車クラスとF1カークラスをPython用に登録する
 */
BOOST_PYTHON_MODULE(pycppinherit) {

    // 車クラスを登録
    boost::python::class_<MyCar>(
        "MyCar",
        boost::python::init<const std::string &, double, int>()
    ).def_readwrite(
        "name",
        &MyCar::name
    ).def_readwrite(
        "mileage",
        &MyCar::mileage
    ).add_property(
        "price",
        &MyCar::getPrice,
        &MyCar::setPrice
    ).def(
        "introduction",
        &MyCar::introduction
    );

    // F1カークラスを登録
    boost::python::class_<F1Car, boost::python::bases<MyCar> >(
        "F1Car",
        boost::python::init<const std::string &, double, int, double>()
    ).def_readwrite(
        "speed",
        &F1Car::speed
    ).def(
        "run",
        &F1Car::run
    );

}
