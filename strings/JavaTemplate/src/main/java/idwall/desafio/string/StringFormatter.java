package idwall.desafio.string;

/**
 * Created by Rodrigo Catão Araujo on 06/02/2018.
 */
public abstract class StringFormatter {

    protected Integer limit;
    protected Boolean justify;

    public StringFormatter() {
        this.limit = 40;
    }

    public StringFormatter(Integer limit) {
        this.limit = limit;
    }

    public StringFormatter(Integer limit, Boolean justify) {
        this.limit = limit;
        this.justify = justify;
    }

    /**
     * It receives a text and should return it formatted
     *
     * @param text
     * @return
     */
    public abstract String format(String text);
}
