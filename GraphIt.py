import matplotlib.pyplot as plot
""" read this for tutorial on using matplotlib 
https://matplotlib.org/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py
https://matplotlib.org/tutorials/introductory/lifecycle.html#sphx-glr-tutorials-introductory-lifecycle-py"""
def graphBar(data,scale=0):
    """ data is a list of dictionary .
    [{x:[],y:[]},{x:[],y:[]},{x:[],y:[]}...]"""
    fg,ax=plot.subplots()
    for pack in data:
        ax.bar(pack['x'],[y/(10**scale) for y in pack['y']])
        mm=list(ax.get_ylim()).extend(pack['y'])
        ax.set_ylim([min(pack['y'])/(10**scale),max(pack['y'])/(10**scale)*1.5])
        plot.setp(ax.get_xticklabels(),fontsize=7,rotation=45, horizontalalignment='right')
        plot.show()
    return fg,ax
