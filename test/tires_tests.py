import unittest
from datetime import datetime

from tires.tires import Tires
from tires.tires_factory import TiresFactory
from tires.tires_options import TiresOptions
from tires.tires_type import TiresType


class TiresTests(unittest.TestCase):
    TIRES_OPTIONS = TiresOptions()
    TIRES_FACTORY = TiresFactory(TIRES_OPTIONS)

    def test_carrigan_dont_need_service(self):
        # Arrange
        tires_wear = [0, 0, 0, 0]
        tires = self.TIRES_FACTORY.create(datetime.today(), tires_wear, TiresType.CARRIGAN)
        # Act
        # Assert
        self.assertFalse(tires.needs_service())

    def test_octoprime_dont_need_service(self):
        # Arrange
        tires_wear = [0, 0, 0, 0]
        tires = self.TIRES_FACTORY.create(datetime.today(), tires_wear, TiresType.OCTOPRIME)
        # Act
        # Assert
        self.assertFalse(tires.needs_service())

    def test_carrigan_dont_need_service_by_total_tires_wear(self):
        # Arrange
        tires_wear = [0.8, 0.8, 0.8, 0.8]
        tires = self.TIRES_FACTORY.create(datetime.today(), tires_wear, TiresType.CARRIGAN)
        # Act
        # Assert
        self.assertFalse(tires.needs_service())

    def test_octoprime_need_service_by_total_tires_wear(self):
        # Arrange
        tires_wear = [0.8, 0.8, 0.8, 0.8]
        tires = self.TIRES_FACTORY.create(datetime.today(), tires_wear, TiresType.OCTOPRIME)
        # Act
        # Assert
        self.assertTrue(tires.needs_service())

    def test_carrigan_need_service_by_single_tire_wear(self):
        # Arrange
        tires_wear = [0.91, 0, 0, 0]
        tires = self.TIRES_FACTORY.create(datetime.today(), tires_wear, TiresType.CARRIGAN)
        # Act
        # Assert
        self.assertTrue(tires.needs_service())

    def test_octoprime_dont_need_service_by_single_tire_wear(self):
        # Arrange
        tires_wear = [0.91, 0, 0, 0]
        tires = self.TIRES_FACTORY.create(datetime.today(), tires_wear, TiresType.OCTOPRIME)
        # Act
        # Assert
        self.assertFalse(tires.needs_service())

