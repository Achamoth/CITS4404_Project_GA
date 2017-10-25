package robocleaner.robot.action;

import robocleaner.robot.IRobot;
import robocleaner.room.IRoom;

import java.util.Random;

/**
 * Created 18/10/2017.
 * 21304455 Alexander Arnold
 * 21492167 Brian Lee
 * 21491901 Zen Ly
 * 21521274 Ammar Abu Shamleh
 */
public class ActionRandom extends AbstractAction {
    public static final ActionRandom instance = new ActionRandom();
    private static final IAction[] pool = new IAction[]{
            ActionUp.instance,
            ActionDown.instance,
            ActionLeft.instance,
            ActionRight.instance
    };
    private static final int poolSize = pool.length;

    private ActionRandom() {
    }

    @Override
    public char getSymbol() {
        return '*';
    }

    @Override
    public void perform(Random rand, IRoom rm, IRobot robot) {
        pool[rand.nextInt(poolSize)].perform(rand, rm, robot);
    }

    @Override
    public IAction getInstance() {
        return instance;
    }
}
