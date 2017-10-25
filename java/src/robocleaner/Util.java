package robocleaner;

/**
 * Created 18/10/2017.
 * 21304455 Alexander Arnold
 * 21492167 Brian Lee
 * 21491901 Zen Ly
 * 21521274 Ammar Abu Shamleh
 */
public class Util {
    public static int pow(int base, int exp) {
        assert exp >= 0;
        if (exp == 0) return 1;
        if (exp == 1) return base;
        if (exp % 2 == 0) return pow(base * base, exp / 2);
        return base * pow(base * base, exp / 2);
    }
}
