%module swiglist

%{
    #include "swiglist.hpp"
%}

%include "std_vector.i"
namespace std {
    %template(IntVector)    vector<int>;
}

extern std::vector<int> bubble_sort(const std::vector<int> &);
