#include <iostream>
#include <string>

int main() {
    int t;
    std::cin >> t;

    while (t--) {
        std::string s;
        std::cin >> s;

        // преобразуем строку в число (до 9e18, иначе использовать long double или BigInteger)
        long long n = std::stoll(s);

        // вычисляем 10^(len-1) целочисленно
        long long power = 1;
        for (size_t i = 1; i < s.length(); ++i) {
            power *= 10;
        }

        std::cout << n - power << '\n';
    }

    return 0;
}
