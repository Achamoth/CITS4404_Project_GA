package robocleaner.robot.action;

import org.jenetics.Gene;
import org.jenetics.util.RandomRegistry;

/**
 * Created 26/10/2017.
 * 21304455 Alexander Arnold
 * 21492167 Brian Lee
 * 21491901 Zen Ly
 * 21521274 Ammar Abu Shamleh
 */
public class IActionGene implements Gene<IAction, IActionGene> {
    protected IAction action;
    protected IAction[] actions;
    public IActionGene(IAction[] actions, int index) {
        this.action = actions[index];
        this.actions = actions;
    }

    /**
     * Make sure action is inside the array
     * @param actions
     * @param action
     */
    public IActionGene(IAction[] actions, IAction action) {
        this.action = action;
        this.actions = actions;
    }

    @Override
    public IAction getAllele() {
        return action;
    }

    @Override
    public IActionGene newInstance() {
        return new IActionGene(actions, RandomRegistry.getRandom().nextInt(actions.length));
    }

    /**
     * Make sure value is inside action array
     * @param value
     * @return
     */
    @Override
    public IActionGene newInstance(IAction value) {
        return new IActionGene(actions, value);
    }

    @Override
    public boolean isValid() {
        return true;
    }

    public IAction[] getActions() {
        return this.actions;
    }

    @Override
    public String toString() {
        return String.valueOf(action.getSymbol());
    }
}
