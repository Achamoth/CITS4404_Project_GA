package robocleaner.robot.action;

import robocleaner.RoboConstants;
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
public class ActionDown extends AbstractAction {
    public static final ActionDown instance = new ActionDown();

    private ActionDown() {
    }

    @Override
    public char getSymbol() {
        return 'D';
    }

    @Override
    public void perform(Random rand, IRoom rm, IRobot robot) {
        int y = robot.getCol() + 1;
        if (!rm.get(robot.getRow(), y).isSolid()) {
            robot.setCol(y);
        } else {
            robot.addPoints(RoboConstants.POINTS_WALL_BUMP);
        }
    }

    @Override
    public IAction getInstance() {
        return instance;
    }
}
