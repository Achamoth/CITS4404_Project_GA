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
public class ActionUp extends AbstractAction {
    public static final ActionUp instance = new ActionUp();

    private ActionUp() {
    }

    @Override
    public char getSymbol() {
        return 'U';
    }

    @Override
    public void perform(Random rand, IRoom rm, IRobot robot) {
        int y = robot.getCol() - 1;
        if (!rm.get(robot.getRow(), y).isSolid()) ;
        robot.setCol(y);
    }

    @Override
    public IAction getInstance() {
        return instance;
    }
}
