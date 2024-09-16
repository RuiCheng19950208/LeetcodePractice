#include <set>
#include <string>
#include <vector>
using namespace std;

#include "LeetcodeHeader.h"
class MyClass
{
public:
    string
    MyClass();
    MyClass(MyClass &&) = default;
    MyClass(const MyClass &) = default;
    MyClass &operator=(MyClass &&) = default;
    MyClass &operator=(const MyClass &) = default;
    ~MyClass();

private:
    
};

MyClass::MyClass()
{
}

MyClass::~MyClass()
{
}