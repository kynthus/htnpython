/******************************************************************************/
/**
 * @addtogroup pycinherit
 * @file       pycinherit.c
 * @brief      Python/C APIにおける継承
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

PyMODINIT_FUNC PyInit_pycinherit(void);

#else

PyMODINIT_FUNC PyInit_pycinherit();

#endif

/* C++互換宣言の終わり */
#if defined(__cplusplus) || defined(c_plusplus)
}
#endif

/**
 * @brief わたしの車クラス
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
 * @brief MyCar構造体のデアロケータ
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
 * @brief  MyCar構造体のコンストラクタ
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

        /* 前設定値を示すポインタが全ビット0のときは、解放処理を行わない */
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
 * @brief  車の値段を取得する
 * @param  self    車の情報を持つインスタンス
 * @param  closure 関連クロージャ(未使用)
 * @return 値段をラップしたPythonのlong型
 */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
static PyObject *my_car_get_price(PyObject *self, void *closure)
#else
static PyObject *my_car_get_price(self, closure)
PyObject *self;
void *closure;
#endif
{

    /* 自身のインスタンスをmy_carとして扱う */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
    const struct my_car *car = (struct my_car *)self;
#else
    struct my_car *car = (struct my_car *)self;
#endif

    /* Pythonのlong型へラップする */
    PyObject *price = PyLong_FromLong((long)car->price);

    /* 引数未使用警告の抑止 */
    (void)closure;

    /* ラッピングに失敗した場合はエラー */
    if (!price) {

        /* 関数エラーリターン */
        return (NULL);

    }

    /* 値段を返す */
    return (price);

}

/**
 * @brief  車の値段を設定する
 * @param  self    車の情報を持つインスタンス
 * @param  value   設定する値段
 * @param  closure 関連クロージャ(未使用)
 * @return 値段をラップしたPythonのlong型
 */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
static int my_car_set_price(PyObject *self, PyObject *value, void *closure)
#else
static int my_car_set_price(self, value, closure)
PyObject *self;
PyObject *value;
void *closure;
#endif
{

    /* 自身のインスタンスをmy_carとして扱う */
    struct my_car *car = (struct my_car *)self;

    /* Pythonの整数型をC言語のlong型へ変換 */
    int price = (int)PyLong_AsLong(value);

    /* 引数未使用警告の抑止 */
    (void)closure;

    /* 値段に負数は許容しない */
    if (price < 0) {

        /* エラーメッセージを表示 */
        PyErr_SetString(PyExc_TypeError, "Cannot setting negative price.");

        /* 負数の場合はエラーとして-1を返す */
        return (-1);

    }

    /* 値段を設定する */
    car->price = price;

    /* 設定が正常に完了したら0を返す */
    return (0);

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

    static struct PyMemberDef attrs[3];

    /* 初期化は初回のみ行う */
    if (is_first) {

        /* 終端のインデックスを計算 */
        size_t end = sizeof(attrs) / sizeof(*attrs) - 1;

        /* 各属性の名称 */
        static char name[] = "name";
        static char mileage[] = "mileage";

        /* 各属性の説明文 */
        static char name_doc[] = "Car name.";
        static char mileage_doc[] = "Car mileage.";

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
 * @brief  アクセッサ情報を初期化して返す
 * @return アクセッサ情報
 */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
static struct PyGetSetDef *my_car_accessor_info(void)
#else
static struct PyGetSetDef *my_car_accessor_info()
#endif
{

    /* 初回呼び出しかどうか(デフォルト:TRUE) */
    static int is_first = 1;

    /* 登録するアクセッサの情報 */
    static struct PyGetSetDef accessors[2];

    /* 初期化は初回のみ行う */
    if (is_first) {

        /* 終端のインデックスを計算 */
        size_t end = sizeof(accessors) / sizeof(*accessors) - 1;

        /* アクセッサの名称と説明文字列 */
        static char price[] = "price";
        static char price_doc[] = "Price's accessor.";

        /* 値段に対するアクセッサの設定 */
        accessors[0].name = price;
        accessors[0].get = my_car_get_price;
        accessors[0].set = my_car_set_price;
        accessors[0].doc = price_doc;
        accessors[0].closure = NULL;

        /* 終端には0およびNULLを設定 */
        accessors[end].name = NULL;
        accessors[end].get = NULL;
        accessors[end].set = NULL;
        accessors[end].doc = NULL;
        accessors[end].closure = NULL;

        /* 2回目以降は初期化しないようにする */
        is_first = !is_first;

    }

    /* アクセッサ情報を返す */
    return (accessors);

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
        type_obj.tp_name = "pycaccess.MyCar";
        type_obj.tp_doc = "My car object.";
        type_obj.tp_basicsize = (Py_ssize_t)sizeof(struct my_car);
        type_obj.tp_itemsize = (Py_ssize_t)0;
        type_obj.tp_flags = Py_TPFLAGS_DEFAULT;
        type_obj.tp_new = PyType_GenericNew;
        type_obj.tp_dealloc = my_car_dealloc;
        type_obj.tp_init = my_car_init;
        type_obj.tp_members = my_car_attrs_info();
        type_obj.tp_methods = my_car_methods_info();
        type_obj.tp_getset = my_car_accessor_info();

        /* 2回目以降は初期化しないようにする */
        is_first = !is_first;

    }

    /* データ型情報を返す */
    return (&type_obj);

}

/**
 * @brief F1カー構造体
 */
struct f1_car {

    /**
     * @brief 基底構造体
     */
    struct my_car base;

    /**
     * @brief 最高速度
     */
    double speed;

};

/**
 * @brief  F1カー構造体のコンストラクタ
 * @param  self   F1カーの情報を持つインスタンス
 * @param  args   コンストラクタの引数
 * @param  kwargs コンストラクタのキーワード引数(未使用)
 * @return 関数の実行結果
 * @retval 0   正常終了
 * @retval 非0 異常終了
 */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
static int f1_car_init(PyObject *self, PyObject *args, PyObject *kwargs)
#else
static int f1_car_init(self, args, kwargs)
PyObject *self;
PyObject *args;
PyObject *kwargs;
#endif
{

    /* 引数の格納先変数 */
    PyObject *name;
    PyObject *mileage;
    PyObject *price;

    /* 基底構造体のコンストラクタへ渡す引数 */
    PyObject *super_args;

    /* 自身のインスタンスをmy_carとして扱う */
    struct f1_car *car = (struct f1_car *)self;

    /* 引数未使用警告の抑止 */
    (void)kwargs;

    /* 引数の解析 */
    if (!PyArg_ParseTuple(args, "OOOd", &name, &mileage, &price, &car->speed)) {

        /* 解析に失敗した場合はエラーとして-1を返す */
        return (-1);

    }

    /* 基底構造体用引数の参照カウントを増やす */
    Py_INCREF(name);
    Py_INCREF(mileage);
    Py_INCREF(price);

    /*
     * 基底構造体のコンストラクタへ渡す引数をまとめる
     * 所有参照なので手動で解放する必要あり
     */
    super_args = PyTuple_Pack((Py_ssize_t)3, name, mileage, price);

    /* タプルの生成に失敗した場合 */
    if (!super_args) {

        /* 基底構造体用引数の参照カウントを減らす */
        Py_DECREF(name);
        Py_DECREF(mileage);
        Py_DECREF(price);

        /* エラーとして-1を返す */
        return (-1);

    }

    /* 基底構造体のコンストラクタ呼出 */
    if (my_car_init(self, super_args, NULL)) {

        /* 引数用タプルを解放 */
        Py_DECREF(super_args);

        /* 基底構造体のコンストラクタが失敗したら-1を返す */
        return (-1);

    }

    /* 引数用タプルを解放 */
    Py_DECREF(super_args);

    /* 初期化が正常に完了したら0を返す */
    return (0);

}

/**
 * @brief  F1カーを走らせる
 * @param  self F1カーの情報を持つインスタンス
 * @param  args 関数・メソッドの引数(未使用)
 * @return 常に「None」を返す
 */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
static PyObject *f1_car_run(PyObject *self, PyObject *args)
#else
static PyObject *f1_car_run(self, args)
PyObject *self;
PyObject *args;
#endif
{

    /* 基底クラスのインスタンス */
    PyObject *base_arg;

    /* 自身のインスタンスをmy_carとして扱う */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
    const struct f1_car *car = (struct f1_car *)self;
    const void *base_ptr = &car->base;
#else
    struct f1_car *car = (struct f1_car *)self;
    void *base_ptr = &car->base;
#endif

    /* 引数未使用警告の抑止 */
    (void)args;

    /* 基底クラスのインスタンスを取得 */
    (void)memcpy(&base_arg, &base_ptr, sizeof(base_arg));

    /* まずは車の紹介 */
    (void)my_car_introduction(base_arg, NULL);

    /* F1カーを走らす */
    (void)printf("3, 2, 1, Go!!! speed[%.1f(km)]\n", car->speed);

    /* 「None」を返して正常リターン */
    Py_RETURN_NONE;

}

/**
 * @brief  F1カーの属性情報を初期化して返す
 * @return F1カーの属性情報
 */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
static struct PyMemberDef *f1_car_attrs_info(void)
#else
static struct PyMemberDef *f1_car_attrs_info()
#endif
{

    /* 初回呼び出しかどうか(デフォルト:TRUE) */
    static int is_first = 1;

    static struct PyMemberDef attrs[2];

    /* 初期化は初回のみ行う */
    if (is_first) {

        /* 終端のインデックスを計算 */
        size_t end = sizeof(attrs) / sizeof(*attrs) - 1;

        /* 各属性の名称 */
        static char speed[] = "speed";

        /* 各属性の説明文 */
        static char speed_doc[] = "Car speed.";

        /* 最高速度の設定 */
        attrs[0].name = speed;
        attrs[0].type = T_DOUBLE;
        attrs[0].offset = (Py_ssize_t)offsetof(struct f1_car, speed);
        attrs[0].flags = 0;
        attrs[0].doc = speed_doc;

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
 * @brief  F1カーのメソッド情報を初期化して返す
 * @return F1カーのメソッド情報
 */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
static struct PyMethodDef *f1_car_methods_info(void)
#else
static struct PyMethodDef *f1_car_methods_info()
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

        /* データ型としてF1カー構造体の情報を設定 */
        methods[0].ml_name = "run";
        methods[0].ml_meth = f1_car_run;
        methods[0].ml_flags = METH_NOARGS;
        methods[0].ml_doc = "Run F1 Car.";

        /* 終端には0およびNULLを設定 */
        methods[end].ml_name = NULL;
        methods[end].ml_meth = NULL;
        methods[end].ml_flags = 0;
        methods[end].ml_doc = NULL;

        /* 2回目以降は初期化しないようにする */
        is_first = !is_first;

    }

    /* メソッド情報を返す */
    return (methods);

}

/**
 * @brief  F1カーのデータ型情報を初期化して返す
 * @return F1カーのデータ型情報
 */
#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
static PyTypeObject *f1_car_type_info(void)
#else
static PyTypeObject *f1_car_type_info()
#endif
{

    /* 初回呼び出しかどうか(デフォルト:TRUE) */
    static int is_first = 1;

    /* モジュール情報を定義し、メソッドを登録 */
    static PyTypeObject type_obj = {PyVarObject_HEAD_INIT(NULL, 0)};

    /* 初期化は初回のみ行う */
    if (is_first) {

        /* データ型としてF1カー構造体の情報を設定 */
        type_obj.tp_name = "pycinherit.F1Car";
        type_obj.tp_doc = "F1 car object.";
        type_obj.tp_basicsize = (Py_ssize_t)sizeof(struct f1_car);
        type_obj.tp_itemsize = (Py_ssize_t)0;
        type_obj.tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE;
        type_obj.tp_init = f1_car_init;
        type_obj.tp_members = f1_car_attrs_info();
        type_obj.tp_methods = f1_car_methods_info();
        type_obj.tp_base = my_car_type_info();

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
static struct PyModuleDef *pycinherit_module_info(void)
#else
static struct PyModuleDef *pycinherit_module_info()
#endif
{

    /* 初回呼び出しかどうか(デフォルト:TRUE) */
    static int is_first = 1;

    /* 呼出元へ返すモジュール情報 */
    static struct PyModuleDef module;

    /* 初期化は初回のみ行う */
    if (is_first) {

        /* モジュール名の設定を行う(メソッドは存在しないためNULL) */
        module.m_name = "pycinherit";
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
PyMODINIT_FUNC PyInit_pycinherit(void)
#else
PyMODINIT_FUNC PyInit_pycinherit()
#endif
{

    /* モジュールとデータ型情報 */
    PyObject *module_info;

    /* 車とF1カーのデータ型情報 */
    PyTypeObject *my_car_info;
    PyTypeObject *f1_car_info;

    /*
     * モジュールオブジェクトを生成して返す
     * 所有参照だが、オブジェクト追加時に盗まれるため手動解放は不要
     * エラー発生時は手動で解放する
     */
    module_info = PyModule_Create(pycinherit_module_info());

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
    my_car_info = my_car_type_info();

    /* 車構造体のデータ型情報をファイナライズ */
    if (PyType_Ready(my_car_info)) {

        /* モジュール情報の解放処理へ */
        goto MODULE_INFO_DEF;

    }

    /* オブジェクトの追加のために参照カウントを増やす */
    Py_INCREF(my_car_info);

    /* モジュール情報へオブジェクトを追加 */
    if (PyModule_AddObject(module_info, "MyCar", (PyObject *)my_car_info)) {

        /* 車構造体の情報を解放する処理へ */
        goto MY_CAR_TYPE_INFO_DEC;

    }

    /*
     * F1カー構造体の情報を取得
     * 正常時には参照カウントを増やし、その際は手動で減らす必要がある
     * エラー発生時は参照カウントを減らしてはならない
     */
    f1_car_info = f1_car_type_info();

    /* データ型情報をファイナライズ */
    if (PyType_Ready(f1_car_info)) {

        /* モジュール情報の解放処理へ */
        goto MODULE_INFO_DEF;

    }

    /* オブジェクトの追加のために参照カウントを増やす */
    Py_INCREF(f1_car_info);

    /* モジュール情報へオブジェクトを追加 */
    if (PyModule_AddObject(module_info, "F1Car", (PyObject *)f1_car_info)) {

        /* F1カー構造体の情報を解放する処理へ */
        goto F1_CAR_TYPE_INFO_DEC;

    }

    /* モジュール情報を返す */
    return (module_info);

    /* F1カー構造体の情報を解放 */
    F1_CAR_TYPE_INFO_DEC:
    Py_DECREF(f1_car_info);

    /* 車構造体の情報を解放 */
    MY_CAR_TYPE_INFO_DEC:
    Py_DECREF(my_car_info);

    /* モジュール情報を解放 */
    MODULE_INFO_DEF:
    Py_DECREF(module_info);

    /* 関数エラーリターン */
    RETURN_NULL:
    return (NULL);

}
