import importlib
import numpy.testing as npt

country = importlib.import_module('.data.03_country-subset', 'src')

interim_data = "data/interim/2018-05-09-winemag_priceGBP.csv"
processed_data = "data/processed/2018-05-15-winemag_Mexico.csv"

def test_get_mean_price():
    mean_price = country.get_mean_price(processed_data)
    assert mean_price == 26.7857
    npt.assert_allclose(country.get_mean_price(processed_data),
                                    26.78577, rtol = 0.01)
