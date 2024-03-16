from llama_index.core.tools import FunctionTool
import matplotlib.pyplot as plt


def save_plot(plot_code, df):
    plot_code
    plt.savefig('tempDir/output.png')

    return "plot saved"


plot_engine = FunctionTool.from_defaults(
    fn=save_plot,
    name="plot_saver",
    description="this tool can save a plot code",
)