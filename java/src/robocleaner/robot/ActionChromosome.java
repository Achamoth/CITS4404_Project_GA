package robocleaner.robot;

import org.jenetics.AbstractChromosome;
import org.jenetics.Chromosome;
import org.jenetics.util.ISeq;
import org.jenetics.util.MSeq;
import org.jenetics.util.RandomRegistry;
import robocleaner.robot.action.IAction;
import robocleaner.robot.action.IActionGene;

import java.util.Random;

/**
 * Created 26/10/2017.
 * 21304455 Alexander Arnold
 * 21492167 Brian Lee
 * 21491901 Zen Ly
 * 21521274 Ammar Abu Shamleh
 */
public class ActionChromosome extends AbstractChromosome<IActionGene> {

    protected IAction[] actions;

    public ActionChromosome(ISeq<IActionGene> genes) {
        super(genes);
        this.actions = genes.get(0).getActions();
    }

    public ActionChromosome(IAction[] actions, int length) {
        this(seq(actions, length));
    }

    @Override
    public Chromosome<IActionGene> newInstance(ISeq<IActionGene> genes) {
        return new ActionChromosome(genes);
    }

    @Override
    public Chromosome<IActionGene> newInstance() {
        return new ActionChromosome(actions, length());
    }

    static ISeq<IActionGene> seq(IAction[] actions, int length) {
        final Random r = RandomRegistry.getRandom();
        return MSeq.<IActionGene>ofLength(length)
                .fill(()-> new IActionGene(actions, r.nextInt(actions.length)))
                .toISeq();
    }

    public IAction[] getActionArray() {
        return this._genes.stream().map((iag -> iag.getAllele())).toArray((len) -> new IAction[len]);
    }
}
