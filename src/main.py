from data_structures.bands_flowchart import BandsFlowchart

if __name__ == '__main__':
    flowchart = list(BandsFlowchart.build(21, 119))

    source_band_id = flowchart[0]
    target_band_id = flowchart[-1]

    print(f'If you like band {source_band_id} and want to like band {target_band_id}, ' \
        'you should listen to the following bands in this order:')

    print(*flowchart, sep=" -> ")
