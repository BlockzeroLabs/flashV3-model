from dataclasses import dataclass
from decimal import Decimal


# x * y = k; a * b = k
# a,b represent token pool amounts, so x,y are not used
# as representations, since which is x or y changes in the equation.
# Store the lower-value-address token as "a" and the other as "b"
@dataclass
class CPI:
    a_address: str
    b_address: str
    a: Decimal
    b: Decimal
    k: Decimal

# ************************************************************************************************
# x = token1_amount                                                                             //
# y = token2_amount                 x * y = k                                                   //
# k = constant_product_invariant                                                                //
# ************************************************************************************************
class AmmCp:

    # ********************************************************************************************
    # x = input_token_liquidity                                                                 //
    # y = output_token_liquidity                  /    k    \                                   //
    # k = constant_product_invariant    oA = y - | --------- |                                  //
    # iA = input_amount                           \  x + iA /                                   //
    # oA = output_amount                                                                        //
    # ********************************************************************************************
    @staticmethod
    def swap(
        input_amount: Decimal,
        input_token_liquidity: Decimal,
        output_token_liquidity: Decimal
    ) -> (Decimal, Decimal, Decimal):
        if input_amount <= 0:
            print('ERROR: INVALID_SWAP_AMOUNT')
            return (Decimal(0), input_token_liquidity, output_token_liquidity)

        # Calculate the amount of output token to return
        k = input_token_liquidity * output_token_liquidity
        output_amount = output_token_liquidity - ((k / (input_token_liquidity + input_amount)))
        # print("output_amount: ", output_amount)

        # Calculate updated liquidity calcs
        updated_input_token_liquidity = input_token_liquidity + input_amount
        updated_output_token_liquidity = output_token_liquidity - output_amount

        # print("swap: ", 
        #     output_amount,
        #     updated_input_token_liquidity,
        #     updated_output_token_liquidity
        # )

        return (
            output_amount,
            updated_input_token_liquidity,
            updated_output_token_liquidity
        )

    @staticmethod
    def swap_cpi(
        token_have: str,
        token_want: str,
        input_amount: Decimal,
        swap_cpi: CPI
    ) -> (Decimal, CPI):
        if input_amount <= 0:
            print('ERROR: INVALID_SWAP_AMOUNT')
            return (Decimal(0), None)

        a_is_have = get_cpi(token_have, swap_cpi)
        if swap_cpi.k == 0:
            print('ERROR: TOKEN_PAIR_NOT_FOUND')
            return (Decimal(0), None)

        # Calculate the amount of wanted token to return
        if a_is_have:
            output_amount = swap_cpi.b - ((swap_cpi.k / (swap_cpi.a + input_amount)))
        else:
            output_amount = swap_cpi.a - ((swap_cpi.k / (swap_cpi.b + input_amount)))

        # Create a CPI with the updated calcs
        updated_cpi = swap_cpi
        updated_cpi.a = swap_cpi.a + input_amount if a_is_have else swap_cpi.a - output_amount
        updated_cpi.b = swap_cpi.b - output_amount if a_is_have else swap_cpi.b + input_amount
        updated_cpi.k = updated_cpi.a * updated_cpi.b

        return (output_amount, updated_cpi)

    # Determine which pool amount variable is the "have" token (input token)
    @staticmethod
    def get_cpi(
        token_have: str,
        swap_cpi: CPI
    ) -> (bool):
        return true if swap_cpi.a_address == token_have else false
