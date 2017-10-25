package robocleaner.robot.action;

/**
 * Created 26/10/2017.
 * 21304455 Alexander Arnold
 * 21492167 Brian Lee
 * 21491901 Zen Ly
 * 21521274 Ammar Abu Shamleh
 */
public abstract class AbstractAction implements IAction {
    @Override
    public String toString() {
        return String.valueOf(this.getSymbol());
    }
}
