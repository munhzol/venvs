        # new Terminal window
        # script=f"""tell application "Terminal"
        #     do script "source {venvs[venvID]['path']}/{venvs[venvID]['name']}/bin/activate"
        #     activate
        #     end tell
        # """

        # script=f"""execCmd("source {venvs[venvID]['path']}/{venvs[venvID]['name']}/bin/activate",1)
        #         on execCmd(cmd, pause)
        #             tell application "System Events"
        #                 tell application process "Terminal"
        #                     set frontmost to true
        #                     keystroke cmd
        #                     keystroke return
        #                 end tell
        #             end tell
        #             delay pause
        #         end execCmd"""

        # script=f"""tell application "System Events"
        #                 tell application process "Terminal"
        #                     set frontmost to true
        #                     keystroke "source {venvs[venvID]['path']}/{venvs[venvID]['name']}/bin/activate"
        #                     keystroke return
        #                 end tell
        #             end tell"""
        
        # script=f"""tell application "System Events"
        #             keystroke "source {venvs[venvID]['path']}/{venvs[venvID]['name']}/bin/activate"
        #             keystroke return
        #            end tell
        #            """

        # script=f"""tell application "System Events"
        #                 keystroke "source {venvs[venvID]['path']}/{venvs[venvID]['name']}/bin/activate"
        #                 keystroke return
        #             end tell"""

        # script=""" tell application "System Events"
        
        #     keystroke "123"
        # end tell"""

        # script="""tell application "Terminal"
        #     if it is running then
        #         keystroke "123"
        #     end if
        # end tell"""

        # tell application "Terminal"
        #   do script "source {venvs[venvID]['path']}/{venvs[venvID]['name']}/bin/activate"
        # end tell

        # 
        #             set currentTab to do script "source {venvs[venvID]['path']}/{venvs[venvID]['name']}/bin/activate"
        #         end tell

        # script=f"""say "You are not listening to me!" using "Bubbles" -- result: spoken in Bubble"""

        # print("source {venvs[venvID]['path']}/{venvs[venvID]['name']}/bin/activate")
        # script=f"""tell application "Terminal"
        #         activate
        #         tell application "System Events" to key code 36 #return
        #     end tell"""


        # new Terminal window
        
        # script=f"""
        #     if application "Terminal" is running then
        #         tell application "System Events"
        #             keystroke "source {venvs[venvID]['path']}/{venvs[venvID]['name']}/bin/activate"
        #             delay 1
        #             keystroke return
        #         end tell
        #     end if
        # """

        # script=f"""tell application "System Events"
                
        #         keystroke "(text returned of aPassword)" & return
        #         delay 1
        #         keystroke return
        #         end tell
        # """
        # applescript.run(script)