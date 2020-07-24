"""
University of Colorado Boulder, SBS Lab
2020
"""
from bs4 import BeautifulSoup


def parse_eplus_html(path):
    """
    parses the energyplus html results file

    parameters
    ----------
    `path`: `str` - the path to the html file.

    returns
    ---------
    a tuple of floats. The first float is
    the total site energy, energy per total building area.
    The second float is total source energy,
    energy per total building area.

    """
    with open(path) as fp:
        soup = BeautifulSoup(fp)

    energy_table = soup.find_all('table')[0]
    rows = energy_table.find_all('tr')
    total_site_energy_data = rows[1]
    total_source_energy_data = rows[3]
    total_site_energy_per_total_building_area_html = total_site_energy_data.find_all('td')[2]
    total_source_energy_per_total_building_area_html = total_source_energy_data.find_all('td')[2]
    total_site_energy_per_total_building_area = float(total_site_energy_per_total_building_area_html.text)
    total_source_energy_per_total_building_area= float(total_source_energy_per_total_building_area_html.text)
    return total_site_energy_per_total_building_area, total_source_energy_per_total_building_area


if __name__ == '__main__':
    result = parse_eplus_html('eplustbl.htm')
    print(result[0], result[1])
