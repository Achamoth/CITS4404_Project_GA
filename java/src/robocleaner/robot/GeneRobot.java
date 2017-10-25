package robocleaner.robot;

import robocleaner.Util;
import robocleaner.robot.action.IAction;
import robocleaner.room.IRoom;
import robocleaner.room.tile.ITile;
import robocleaner.room.view.IView;

import java.security.InvalidParameterException;
import java.util.Arrays;
import java.util.Set;

/**
 * Created 18/10/2017.
 * 21304455 Alexander Arnold
 * 21492167 Brian Lee
 * 21491901 Zen Ly
 * 21521274 Ammar Abu Shamleh
 */
public class GeneRobot extends BaseRobot {

    public IAction[] gene = new IAction[0];

    public GeneRobot(Set<IAction> actionSet, IRoom room, IView view, int x, int y) {
        super(actionSet, room, view, x, y);
        clearGene();
    }

    public void clearGene() {
        gene = new IAction[Util.pow(getRoom().getTileSet().size(), getView().getSize())];
    }

    public void loadGene(IAction[] actions) {
        clearGene();
        if (actions.length != gene.length)
            throw new InvalidParameterException(
                    "Expected actions array of length " + gene.length + " but got array of length " + actions.length);
        gene = Arrays.copyOf(actions, gene.length);
    }

    @Override
    public IAction getAction() {
        int index = 0;
        int tileSize = getRoom().getTileSet().size();
        for (ITile tile : getView().getTiles(getRoom(), getRow(), getCol())) {
            index *= tileSize;
            index += getRoom().getTileIndex(tile);
        }
        return gene[index];
    }
}
