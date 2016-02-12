#include <nowide/convert.hpp>
#include <iostream>
#include <string>

int main()
{
    std::wstring str_wide(L"test");
    std::string str_narrow = nowide::narrow(str_wide);
    if (str_narrow != "test") {
        return 1;
    }

    return 0;
}
