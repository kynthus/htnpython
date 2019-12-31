/******************************************************************************/
/**
 * @addtogroup pyccar
 * @file       pyccar.c
 * @brief      Python/C APIにおけるクラス(属性とメソッド持ち)
 * @date       2019-12-08
 * @author     Hatano Yusuke
 */
/******************************************************************************/

/**
 * @brief サイズ値をintではなく、ssize_tで扱うためのマクロ
 */
#define PY_SSIZE_T_CLEAN

/* Python API用のヘッダ */
#include <Python.h>
#include <structmember.h>

/* C++互換宣言の始まり */
#if defined(__cplusplus) || defined(c_plusplus)
extern "C" {
#endif

/* 関数のプロトタイプ宣言 */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)

PyMODINIT_FUNC PyInit_pyccar(void);

#else

PyMODINIT_FUNC PyInit_pyccar();

#endif

/* C++互換宣言の終わり */
#if defined(__cplusplus) || defined(c_plusplus)
}
#endif

/**
 * @brief わたしの車構造体
 */
struct my_car {

    /* Python互換用の基本メンバ */
    PyObject_HEAD

    /**
     * @brief 車種
     */
    PyObject *name;

    /**
     * @brief 走行距離
     */
    double mileage;

    /**
     * @brief 値段
     */
    int price;

};

/**
 * @brief 車構造体のデアロケータ
 * @param self 解放対象のインスタンス
 */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
static void my_car_dealloc(PyObject *self)
#else
static void my_car_dealloc(self)
PyObject *self;
#endif
{

    /* 車種を比較する際に使用するポインタ */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
    const void *zeroes;
#else
    void *zeroes;
#endif

    /* 自身のインスタンスをmy_carとして扱う */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
    const struct my_car *car = (struct my_car *)self;
#else
    struct my_car *car = (struct my_car *)self;
#endif

    /* 比較用のポインタを0埋めする */
    (void)memset(&zeroes, 0x00, sizeof(zeroes));

    /* 車種を示すポインタが全ビット0のときは、解放処理を行わない */
    if (memcmp(&car->name, &zeroes, sizeof(car->name))) {

        /* 車種を解放 */
        Py_XDECREF(car->name);

    }

    /* オブジェクトを解放する */
    self->ob_type->tp_free(self);

}

/**
 * @brief  車構造体のコンストラクタ
 * @param  self   車の情報を持つインスタンス
 * @param  args   コンストラクタの引数
 * @param  kwargs コンストラクタのキーワード引数(未使用)
 * @return 関数の実行結果
 * @retval 0   正常終了
 * @retval 非0 異常終了
 */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
static int my_car_init(PyObject *self, PyObject *args, PyObject *kwargs)
#else
static int my_car_init(self, args, kwargs)
PyObject *self;
PyObject *args;
PyObject *kwargs;
#endif
{

    /* 引数の格納先変数 */
    PyObject *name;

    /* 自身のインスタンスをmy_carとして扱う */
    struct my_car *car = (struct my_car *)self;

    /* 引数未使用警告の抑止 */
    (void)kwargs;

    /* 引数の解析 */
    if (!PyArg_ParseTuple(args, "Odi", &name, &car->mileage, &car->price)) {

        /* 解析に失敗した場合はエラーとして-1を返す */
        return (-1);

    }

    /* PyObjectの場合は前設定値の解放が必要 */
    if (name) {

        /* 前設定値を比較する際に使用するポインタ */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
        const void *zeroes;
#else
        void *zeroes;
#endif

        /* 前設定値を取得 */
        PyObject *tmp = car->name;

        /* 比較用のポインタを0埋めする */
        (void)memset(&zeroes, 0x00, sizeof(zeroes));

        /* 前設定値が全ビット0のときは、解放処理を行わない */
        if (memcmp(&car->name, &zeroes, sizeof(car->name))) {

            /* 前設定値を解放 */
            Py_XDECREF(tmp);

        }

        /* 参照カウントを増やし、車種を設定 */
        Py_INCREF(name);
        car->name = name;

    }

    /* 初期化が正常に完了したら0を返す */
    return (0);

}

/**
 * @brief  車の情報を表示する
 * @param  self 車の情報を持つインスタンス
 * @param  args 関数・メソッドの引数(未使用)
 * @return 常に「None」を返す
 */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
static PyObject *my_car_introduction(PyObject *self, PyObject *args)
#else
static PyObject *my_car_introduction(self, args)
PyObject *self;
PyObject *args;
#endif
{

    /* UTF-8へ変換時の文字列長 */
    Py_ssize_t length;

    /* 自身のインスタンスをmy_carとして扱う */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
    const struct my_car *car = (struct my_car *)self;
#else
    struct my_car *car = (struct my_car *)self;
#endif

    /* 車種を文字列として入手 */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
    const char *name = PyUnicode_AsUTF8AndSize(car->name, &length);
#else
    char *name = PyUnicode_AsUTF8AndSize(car->name, &length);
#endif

    /* 引数未使用警告の抑止 */
    (void)args;

    /* 車種の取得に失敗した場合はエラー */
    if (!name) {

        /* 関数エラーリターン */
        return (NULL);

    }

    /* 車情報を表示する */
    (void)printf("My car's information [name: %s, mileage: %f, price: %d]\n", name, car->mileage, car->price);

    /* 「None」を返して正常リターン */
    Py_RETURN_NONE;

}

/**
 * @brief  属性情報を初期化して返す
 * @return 属性情報
 */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
static struct PyMemberDef *my_car_attrs_info(void)
#else
static struct PyMemberDef *my_car_attrs_info()
#endif
{

    /* 初回呼び出しかどうか(デフォルト:TRUE) */
    static int is_first = 1;

    static struct PyMemberDef attrs[4];

    /* 初期化は初回のみ行う */
    if (is_first) {

        /* 終端のインデックスを計算 */
        size_t end = sizeof(attrs) / sizeof(*attrs) - 1;

        /* 各属性の名称 */
        static char name[] = "name";
        static char mileage[] = "mileage";
        static char price[] = "price";

        /* 各属性の説明文 */
        static char name_doc[] = "Car name.";
        static char mileage_doc[] = "Car mileage.";
        static char price_doc[] = "Car price.";

        /* 車種の設定 */
        attrs[0].name = name;
        attrs[0].type = T_OBJECT_EX;
        attrs[0].offset = (Py_ssize_t)offsetof(struct my_car, name);
        attrs[0].flags = 0;
        attrs[0].doc = name_doc;

        /* 走行距離の設定 */
        attrs[1].name = mileage;
        attrs[1].type = T_DOUBLE;
        attrs[1].offset = (Py_ssize_t)offsetof(struct my_car, mileage);
        attrs[1].flags = 0;
        attrs[1].doc = mileage_doc;

        /* 値段の設定 */
        attrs[2].name = price;
        attrs[2].type = T_INT;
        attrs[2].offset = (Py_ssize_t)offsetof(struct my_car, price);
        attrs[2].flags = 0;
        attrs[2].doc = price_doc;

        /* 終端には0およびNULLを設定 */
        attrs[end].name = NULL;
        attrs[end].type = 0x00;
        attrs[end].offset = (Py_ssize_t)0x00;
        attrs[end].flags = 0x00;
        attrs[end].doc = NULL;

        /* 2回目以降は初期化しないようにする */
        is_first = !is_first;

    }

    /* 属性情報を返す */
    return (attrs);

}

/**
 * @brief  メソッド情報を初期化して返す
 * @return メソッド情報
 */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
static struct PyMethodDef *my_car_methods_info(void)
#else
static struct PyMethodDef *my_car_methods_info()
#endif
{

    /* 初回呼び出しかどうか(デフォルト:TRUE) */
    static int is_first = 1;

    /* 登録するメソッドの情報 */
    static struct PyMethodDef methods[2];

    /* 初期化は初回のみ行う */
    if (is_first) {

        /* 終端のインデックスを計算 */
        size_t end = sizeof(methods) / sizeof(*methods) - 1;

        /* データ型として車構造体の情報を設定 */
        methods[0].ml_name = "introduction";
        methods[0].ml_meth = my_car_introduction;
        methods[0].ml_flags = METH_NOARGS;
        methods[0].ml_doc = "Introduce you to my car.";

        /* 終端には0およびNULLを設定 */
        methods[end].ml_name = NULL;
        methods[end].ml_meth = NULL;
        methods[end].ml_flags = 0x00;
        methods[end].ml_doc = NULL;

        /* 2回目以降は初期化しないようにする */
        is_first = !is_first;

    }

    /* メソッド情報を返す */
    return (methods);

}

/**
 * @brief  データ型情報を初期化して返す
 * @return データ型情報
 */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
static PyTypeObject *my_car_type_info(void)
#else
static PyTypeObject *my_car_type_info()
#endif
{

    /* 初回呼び出しかどうか(デフォルト:TRUE) */
    static int is_first = 1;

    /* モジュール情報を定義し、メソッドを登録 */
    static PyTypeObject type_obj = {PyVarObject_HEAD_INIT(NULL, 0)};

    /* 初期化は初回のみ行う */
    if (is_first) {

        /* データ型として車構造体の情報を設定 */
        type_obj.tp_name = "pyccar.MyCar";
        type_obj.tp_doc = "My car object.";
        type_obj.tp_basicsize = (Py_ssize_t)sizeof(struct my_car);
        type_obj.tp_itemsize = (Py_ssize_t)0;
        type_obj.tp_flags = Py_TPFLAGS_DEFAULT;
        type_obj.tp_new = PyType_GenericNew;
        type_obj.tp_dealloc = my_car_dealloc;
        type_obj.tp_init = my_car_init;
        type_obj.tp_members = my_car_attrs_info();
        type_obj.tp_methods = my_car_methods_info();

        /* 2回目以降は初期化しないようにする */
        is_first = !is_first;

    }

    /* データ型情報を返す */
    return (&type_obj);

}

/**
 * @brief  モジュール情報を初期化して返す
 * @return モジュール情報
 */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
static struct PyModuleDef *pyccar_module_info(void)
#else
static struct PyModuleDef *pyccar_module_info()
#endif
{

    /* 初回呼び出しかどうか(デフォルト:TRUE) */
    static int is_first = 1;

    /* 呼出元へ返すモジュール情報 */
    static struct PyModuleDef module;

    /* 初期化は初回のみ行う */
    if (is_first) {

        /* モジュール名の設定を行う(メソッドは存在しないためNULL) */
        module.m_name = "pyccar";
        module.m_doc = "Python C API Test module";
        module.m_size = (Py_ssize_t)-1;
        module.m_methods = NULL;

        /* 2回目以降は初期化しないようにする */
        is_first = !is_first;

    }

    /* モジュール情報を返す */
    return (&module);

}

/**
 * @brief  Pythonモジュールの初期化を行う
 * @return Pythonのモジュールオブジェクト
 */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
PyMODINIT_FUNC PyInit_pyccar(void)
#else
PyMODINIT_FUNC PyInit_pyccar()
#endif
{

    /* モジュールとデータ型情報 */
    PyObject *module_info;
    PyTypeObject *type_info;

    /*
     * モジュールオブジェクトを生成して返す
     * 所有参照だが、オブジェクト追加時に盗まれるため手動解放は不要
     * エラー発生時は手動で解放する
     */
    module_info = PyModule_Create(pyccar_module_info());

    /* モジュールオブジェクトの生成に失敗した場合はエラー */
    if (!module_info) {

        /* NULLリターンへ */
        goto RETURN_NULL;

    }

    /*
     * 車構造体の情報を取得
     * 正常時には参照カウントを増やし、その際は手動で減らす必要がある
     * エラー発生時は参照カウントを減らしてはならない
     */
    type_info = my_car_type_info();

    /* データ型情報をファイナライズ */
    if (PyType_Ready(type_info)) {

        /* モジュール情報の解放処理へ */
        goto MODULE_INFO_DEF;

    }

    /* オブジェクトの追加のために参照カウントを増やす */
    Py_INCREF(type_info);

    /* モジュール情報へオブジェクトを追加 */
    if (PyModule_AddObject(module_info, "MyCar", (PyObject *)type_info)) {

        /* 車構造体の情報を解放する処理へ */
        goto TYPE_INFO_DEC;

    }

    /* モジュール情報を返す */
    return (module_info);

    /* 車構造体の情報を解放 */
    TYPE_INFO_DEC:
    Py_DECREF(type_info);

    /* モジュール情報を解放 */
    MODULE_INFO_DEF:
    Py_DECREF(module_info);

    /* 関数エラーリターン */
    RETURN_NULL:
    return (NULL);

}
