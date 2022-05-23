import os

import matplotlib.pyplot as plt

class TuningUp:
    def __init__(self, chapter, base_dir = "/Users/dsweet2/Desktop/Tuning Up"):
        assert os.path.exists(base_dir), f"Directory {base_dir} does not exists"
        self.chapter = chapter
        if isinstance(chapter, str):
            self.fig_dir = f"{base_dir}/Appendix {chapter}/"
        else:
            self.fig_dir = f"{base_dir}/Chapter {chapter}/"
        self.clr1 = "#444444"
        self.clr2 = "#777777"
        self.clr3 = "#AAAAAA"
        self.clr4 = "#DDDDDD"
        self.clrs = [self.clr1, self.clr2, self.clr3, self.clr4]
        self.alpha_err = .333
        self.arrow_props = {'width':1, 'color': self.clr1,
                            'headwidth': 5, 'headlength': 7}
        self.font_size_2d = 7

        os.makedirs(self.fig_dir, exist_ok=True)


    def save_fig_named(self, name):
        plt.tight_layout()
        for ext in ["eps", "png"]:
            try:
                fmt = f"{self.chapter:02d}"
            except Exception:
                fmt = self.chapter
            plt.savefig(f"{self.fig_dir}/CH{fmt}_{name}_sweet.{ext}")

    def save_fig(self, fig_num):
        self.save_fig_named(f"F{fig_num:02d}")

    def aspect_square(self, ax):
        c = ax.axis()
        ax.set_aspect((c[1]-c[0]) / (c[3]-c[2]))

    def horizontal_line(self, y0, clr=None):
        if clr is None:
            clr = self.clr3
        c = plt.axis()
        plt.autoscale(False)
        plt.plot([c[0], c[1]], [y0, y0], '--', linewidth=1, color=clr)
        
    def vertical_line(self, x0, clr=None, ax=plt):
        if clr is None:
            clr = self.clr3
        c = ax.axis()
        ax.autoscale(False)
        ax.plot([x0, x0], [c[2], c[3]], '--', linewidth=1, color=clr)
        
    def err_plot(self, m, se, x=None, color=None, ax=plt):
        if x is None:
            x = np.arange(len(m))
        if color is None:
            color = self.clr2
        ax.fill_between(
            x,
            m - 2*se,
            m + 2*se,
            color=color, alpha=alpha_err, linewidth=1
        )
