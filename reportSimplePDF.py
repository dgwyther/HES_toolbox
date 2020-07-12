import pandas as pd
import plotly.graph_objects as go
import plotly
from fpdf import FPDF

title = 'Example title that is about the same length '
author = 'Example author and date'
logo_path = 'assets/logo.png'
output_name = 'test.pdf'

stats_notes = 'This bit can include any special notes that you want to make about the statistics in this report. e.g. Note erroneous data arising due to blah blah. This will be automatically added as a special note to the end of the statistics summary section.'


# Load data
df_SS=
df_SRES=
# Trim data

# Alias data

# which plots to make?
timeseries_plots = ["SensorRel_Max(1)",
                    "SensorRel_Max(2)",
                    "SensorRel_Max(3)",
                    "SensorRel_Max(4)",
                    "SensorRel_Max(5)"]

x_y_plots = [""]

invNorm_plots = ["S_P2_CH_R_HJCrack_Pkp",
                    "S_P2_CH_L_HJCrack_Pkp",
                    "S_S2_G1_Pkp",
                    "S_S2_G2_Pkp",
                    "S_S2_G3_Pkp"]

## GENERATE TABLES

## GENERATE PLOTS
# plot_timeseriesNoZoom
traces = []
for var in timeseries_plots:
    traces.append(go.Scatter(x=df_SS['TIMESTAMP'], 
                        y=df_SS[var],
                        mode="lines",
                        name=var,
                        marker=dict(size=2)
        ))
    fig1 = go.Figure(data=traces)
# Add shape regions
    fig1.update_layout(
        shapes=[
            # 1st highlight during Feb 4 - Feb 6
            dict(
                type="rect",
                # x-reference is assigned to the x-values
                xref="x",
                # y-reference is assigned to the plot paper [0,1]
                yref="paper",
                x0=pd.to_datetime(df_SS['TIMESTAMP'].max())-datetime.timedelta(days=14),
                y0=0,
                x1=pd.to_datetime(df_SS['TIMESTAMP'].max()),
                y1=1,
                fillcolor="LightSalmon",
                opacity=0.5,
                layer="below",
                line_width=0,
            )

        ]
    )

## DEFINE CLASSES
class PDF(FPDF):
    def header(self):
        # Logo
        self.image(logo_path, 170, 8, 33)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Calculate width of title and position
        w = self.get_string_width(title) + 6
        self.set_x((210 - w) / 2)
        # Colors of frame, background and text
#        self.set_draw_color(0, 80, 180)
#        self.set_fill_color(230, 230, 0)
#        self.set_text_color(220, 50, 50)
#        # Thickness of frame (1 mm)
#        self.set_line_width(1)
        # Title
        self.cell(w, 9, title, 0, 0, 'C')
        # Line break
        self.ln(10)
        # Author and date
        self.cell(w, 9, author, 0, 0, 'R')        
        # Line break
        self.ln(20)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Text color in gray
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def section_title(self, num, label):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, 'Section %d : %s' % (num, label), 0, 1, 'L', 1)
        # Line break
        self.ln(4)

    def section_body(self, name):
        # Read text file
        with open(name, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        # Times 12
        self.set_font('Times', '', 12)
        # Output justified text
        self.multi_cell(0, 5, txt)
        # Line break
        self.ln()
#        # Mention in italics
#        self.set_font('', 'I')
#        self.cell(0, 5, '(end of excerpt)')

# this will plot a section of text.
    def print_textSection(self, num, title, text_fill):
        self.add_page()
        self.section_title(num, title)
        self.section_body(text_fill)
# this will add the stats section with tables.
    def print_statsSection(self, num, title):
        self.add_page()
        self.section_title(num, title)
        #add auto generated tabulated data here
        #add text here from a 'stats_notes='
# this adds a new section with section header        
    def print_sectionHeader(self, num, title):
        self.add_page()
        self.section_title(num, title)
        
## COMPILE PDF

pdf = PDF()
pdf.set_title(title)
pdf.set_author(author)
pdf.print_statsSection(1, 'Summary statistics')
pdf.print_sectionHeader(2, 'Timeseries data')
# Add time series plots
pdf.print_sectionHeader(3, 'X-Y data')
# Add X-Y data plot
pdf.print_sectionHeader(4, 'Inverse normal plots')
# Add inverse normal plots
pdf.output(output_name, 'F')