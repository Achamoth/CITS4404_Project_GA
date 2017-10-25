package robocleaner.robot.action;

import robocleaner.RoboConstants;
import robocleaner.robot.IRobot;
import robocleaner.room.IRoom;
import robocleaner.room.tile.ITile;
import robocleaner.room.tile.TileEmpty;

import java.util.Random;

/**
 * Created 18/10/2017.
 * 21304455 Alexander Arnold
 * 21492167 Brian Lee
 * 21491901 Zen Ly
 * 21521274 Ammar Abu Shamleh
 */
public class ActionPickUp extends AbstractAction {
    public static final ActionPickUp instance = new ActionPickUp();

    private ActionPickUp() {
    }

    @Override
    public char getSymbol() {
        return '^';
    }

    @Override
    public void perform(Random rand, IRoom rm, IRobot robot) {
        int r = robot.getRow();
        int c = robot.getCol();
        ITile tile = rm.get(r, c);
        if(tile.isCollectable()) {
            robot.addPoints(tile.getPoints());
            rm.set(r, c, TileEmpty.instance);
        } else {
            robot.addPoints(RoboConstants.POINTS_NON_COLLECTABLE);
        }
    }

    @Override
    public IAction getInstance() {
        return instance;
    }
}
