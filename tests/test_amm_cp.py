import unittest
from decimal import Decimal

from model.parts.amm_cp import AmmCp


class TestAmmCp(unittest.TestCase):
    def test_exact_input(self):
        exact_input = {
            'ia': Decimal('50'),
            'th_liq': Decimal('100000'),
            'tw_liq': Decimal('100000')
        }
        (output_amount,
            updated_input_token_liquidity,
            updated_output_token_liquidity
        ) = AmmCp.swap(
            input_amount=exact_input['ia'],
            input_token_liquidity=exact_input['th_liq'],
            output_token_liquidity=exact_input['tw_liq']
        )
        print(output_amount, updated_input_token_liquidity, updated_output_token_liquidity)

        # output = y - (k / (x + input))
        k = exact_input['th_liq'] * exact_input['tw_liq']
        output = exact_input['tw_liq'] - (k / (exact_input['th_liq'] + exact_input['ia']))
        print(output)

        self.assertEqual(output_amount, output)

if __name__ == '__main__':
    unittest.main()
