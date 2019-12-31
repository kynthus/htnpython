CC = g++
CFLAGS = \
	-fPIC \
	-ansi \
	-pedantic-errors \
	-Wabi \
	-Wabi-tag \
	-Waddress \
	-Waggregate-return \
	-Waggressive-loop-optimizations \
	-Waliasing \
	-Walign-commons \
	-Wall \
	-Wampersand \
	-Warray-bounds \
	-Warray-temporaries \
	-Wassign-intercept \
	-Wattributes \
	-Wbad-function-cast \
	-Wbuiltin-macro-redefined \
	-Wc++-compat \
	-Wc++0x-compat \
	-Wc++11-compat \
	-Wc-binding-type \
	-Wcast-align \
	-Wcast-qual \
	-Wchar-subscripts \
	-Wcharacter-truncation \
	-Wclobbered \
	-Wcomment \
	-Wcomments \
	-Wcompare-reals \
	-Wconversion \
	-Wconversion-extra \
	-Wconversion-null \
	-Wcoverage-mismatch \
	-Wcpp \
	-Wctor-dtor-privacy \
	-Wdeclaration-after-statement \
	-Wdelete-non-virtual-dtor \
	-Wdeprecated \
	-Wdeprecated-declarations \
	-Wdisabled-optimization \
	-Wdiv-by-zero \
	-Wdouble-promotion \
	-Weffc++ \
	-Wempty-body \
	-Wendif-labels \
	-Wenum-compare \
	-Werror-implicit-function-declaration \
	-Wextra \
	-Wfloat-equal \
	-Wformat \
	-Wformat-contains-nul \
	-Wformat-extra-args \
	-Wformat-nonliteral \
	-Wformat-security \
	-Wformat-y2k \
	-Wformat-zero-length \
	-Wfree-nonheap-object \
	-Wfunction-elimination \
	-Wignored-qualifiers \
	-Wimplicit \
	-Wimplicit-function-declaration \
	-Wimplicit-int \
	-Wimplicit-interface \
	-Wimplicit-procedure \
	-Winherited-variadic-ctor \
	-Winit-self \
	-Winline \
	-Wint-to-pointer-cast \
	-Wintrinsic-shadow \
	-Wintrinsics-std \
	-Winvalid-memory-model \
	-Winvalid-offsetof \
	-Winvalid-pch \
	-Wjump-misses-init \
	-Wlarger-than=4096 \
	-Wline-truncation \
	-Wliteral-suffix \
	-Wlogical-op \
	-Wlong-long \
	-Wmain \
	-Wmaybe-uninitialized \
	-Wmissing-braces \
	-Wmissing-declarations \
	-Wmissing-field-initializers \
	-Wmissing-include-dirs \
	-Wmissing-parameter-type \
	-Wmissing-prototypes \
	-Wmudflap \
	-Wmultichar \
	-Wnarrowing \
	-Wnested-externs \
	-Wnoexcept \
	-Wnon-template-friend \
	-Wnon-virtual-dtor \
	-Wnonnull \
	-Wold-style-cast \
	-Wold-style-declaration \
	-Wold-style-definition \
	-Woverflow \
	-Woverlength-strings \
	-Woverloaded-virtual \
	-Woverride-init \
	-Wpacked \
	-Wpacked-bitfield-compat \
	-Wpadded \
	-Wparentheses \
	-Wpedantic \
	-Wpmf-conversions \
	-Wpointer-arith \
	-Wpointer-sign \
	-Wpointer-to-int-cast \
	-Wpragmas \
	-Wproperty-assign-default \
	-Wprotocol \
	-Wreal-q-constant \
	-Wrealloc-lhs \
	-Wrealloc-lhs-all \
	-Wredundant-decls \
	-Wreorder \
	-Wreturn-local-addr \
	-Wreturn-type \
	-Wselector \
	-Wsequence-point \
	-Wshadow \
	-Wsign-compare \
	-Wsign-promo \
	-Wsizeof-pointer-memaccess \
	-Wstack-protector \
	-Wstack-usage=512 \
	-Wstrict-aliasing \
	-Wstrict-null-sentinel \
	-Wstrict-overflow \
	-Wstrict-prototypes \
	-Wstrict-selector-match \
	-Wsuggest-attribute=const \
	-Wsuggest-attribute=format \
	-Wsuggest-attribute=noreturn \
	-Wsuggest-attribute=pure \
	-Wsurprising \
	-Wswitch \
	-Wswitch-default \
	-Wswitch-enum \
	-Wsync-nand \
	-Wsynth \
	-Wtabs \
	-Wtarget-lifetime \
	-Wtraditional \
	-Wtraditional-conversion \
	-Wtrampolines \
	-Wtrigraphs \
	-Wtype-limits \
	-Wundeclared-selector \
	-Wundef \
	-Wunderflow \
	-Wuninitialized \
	-Wunknown-pragmas \
	-Wunsafe-loop-optimizations \
	-Wunsuffixed-float-constants \
	-Wunused \
	-Wunused-but-set-parameter \
	-Wunused-but-set-variable \
	-Wunused-dummy-argument \
	-Wunused-function \
	-Wunused-label \
	-Wunused-local-typedefs \
	-Wunused-macros \
	-Wunused-parameter \
	-Wunused-result \
	-Wunused-value \
	-Wunused-variable \
	-Wuseless-cast \
	-Wvarargs \
	-Wvariadic-macros \
	-Wvector-operation-performance \
	-Wvirtual-move-assign \
	-Wvla \
	-Wvolatile-register-var \
	-Wwrite-strings \
	-Wzero-as-null-pointer-constant \
	-frequire-return-statement \


SO = $(CC)
SFLAGS = -shared

OBJS = ctphello.o

TARGET = libctphello
SHARED = $(TARGET).so

all : $(SHARED)

install : all
	cp -ip $(SHARED) /usr/local/lib

clean :
	rm *.o $(SHARED)

$(SHARED) : $(OBJS)
	$(SO) $(SFLAGS) -o $(SHARED) $(OBJS)

.c.o :
	$(CC) -c $(CFLAGS) -o $@ $<

.cpp.o :
	$(CC) -c $(CFLAGS) -o $@ $<
