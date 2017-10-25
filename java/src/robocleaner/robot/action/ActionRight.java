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
public class ActionRight extends AbstractAction {
    public static final ActionRight instance = new ActionRight();

    private ActionRight() {
    }

    @Override
    public char getSymbol() {
        return 'R';
    }

    @Override
    public void perform(Random rand, IRoom rm, IRobot robot) {
        int x = robot.getRow() + 1;
        if (!rm.get(x, robot.getCol()).isSolid()) ;
        robot.setRow(x);
    }

    @Override
    public IAction getInstance() {
        return instance;
    }
}