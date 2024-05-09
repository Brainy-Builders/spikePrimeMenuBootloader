# This file is part of the Spike Prime Menu Bootloader which is released under BSL 1.0.
# See file LICENSE or go to https://www.boost.org/users/license.html for full license details.

import runloop
from hub import button, light_matrix
import time

async def main(data):
    _index = 0
    while True:
        if (button.pressed(button.LEFT) and button.pressed(button.RIGHT)):
            _index -= 1 # Debounce bug
            name = data[_index % len(data)][0]
            usesAsync = data[_index % len(data)][1]
            print
            if (usesAsync):
                await name()
            else:
                name()
                
            _index += 1 # Menu auto increment
        elif button.pressed(button.LEFT) and not button.pressed(button.RIGHT):
            _index -= 1
            await runloop.sleep_ms(250)
        elif button.pressed(button.RIGHT) and not button.pressed(button.LEFT):
            _index += 1
            await runloop.sleep_ms(250)
        light_matrix.show(data[_index%len(data)][2])
        
        await runloop.sleep_ms(10)



runloop.run(
    main(LOADED_FILES_LIST)
)