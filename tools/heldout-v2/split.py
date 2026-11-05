# Video-level split. TRAIN induces rules, VAL accepts/rejects them, TEST is only used for the final exams.
TRAIN={'adam/01-ai-disaster','adam/02-bestselling-book','gen/1','gen/2','gen/3','gen/4','gen/5','esp/01-spacex',
 'after/01-dark-side-data-centers','after/02-greed','after/03-recycling','after/04-pov-ai','after/05-middle-class','after/06-diamonds'}
VAL={'adam/03-no-longer-in-control','gen/6','gen/7','esp/02-ai-paradox','after/07-trump-family','after/08-tokens','after/09-microchip-war'}
TEST={'adam/04-superintelligence','adam/05-sam-altman','gen/8','gen/9','gen/10','esp/03-oil-apocalypse','esp/06-data-centers',
 'after/10-water','after/11-anthropic-ipo','after/12-data-centres-not-working'}
def part(key): return 'train' if key in TRAIN else 'val' if key in VAL else 'test'
