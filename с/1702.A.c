#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    int t;
    scanf("%d", &t);                 // количество тестов

    while (t--) {
        char s[100];                  // строка для числа (достаточно для 20 цифр)
        scanf("%s", s);                // читаем число как строку

        int len = strlen(s);           // длина строки
        long long num = strtoll(s, NULL, 10);  // преобразуем в число
        long long power = 1;            // 10^(len-1)

        for (int i = 1; i < len; i++) {
            power *= 10;
        }

        printf("%lld\n", num - power);  // выводим результат
    }

    return 0;
}
