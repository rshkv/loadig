from sys import stdout


class Bar():

    """Use this class to display progress. 
    Make sure your command line interface understands ANSI escape codes.
    """

    def __init__(self, total=100, characters=40, message=None):
        """
        total       (optional) the highest number representing 100%
        characters  (optional) the number of characters to print between the brackets
        message     (optional) inital message
        """
        self.total = total - 1  # Because most iterators go from 0 to len - 1
        self.chars = characters - 2  # subtract two brackets
        self.percentage = 0
        self.message = self._clean_message(message)
        self.done = False  # To check if further printing is necessary
        # Print message if given, otherwise just an empty bar
        if message:  # Print message if given
            stdout.write(self.message + "\n")
        #  Print empty bar
        stdout.write("\r[%s]  0%%" % (" " * self.chars))

    def update(self, value=None):
        """Updates the bar. Pass either a string or a number. 
        If you pass a string, it will be used to change the dislpayed message.
        If you pass a number, the left to right progress and percentage will change.
        """
        if self.done:  # Return if no further printing is necessary
            return

        # If 'value' is a str update the message above the bar
        if isinstance(value, str):
            self._update_message(value)

        # Otherwise update progress
        else:
            self._update_progress(value)

    def clear(self):
        """Erase everything and move cursor to first position.
        """
        clear_string = ""
        if self.done:
            # Move up a line if progress ended and a new line was opened
            clear_string += "\033[F"
        clear_string += "\r\033[K"  # Delete the line with the bar
        if self.message:
            # Move up a line if a message was shown
            clear_string += "\033[F\033[K"
        stdout.write(clear_string)
        # Initialize state
        self.done = False
        self.percentage = 0
        self.message = None

    @staticmethod
    def _clean_message(msg):
        """Make sure the message has no new lines, and is not longer than 80
        characters.
        """
        msg = msg.replace("\n", "")
        msg = msg[:80]
        return msg

    def _update_message(self, msg):
        """Update message dislpayed above bar.
        """
        msg = self._clean_message(msg)
        if self.message:
            # If there was a message before go up a line
            stdout.write("\033[F")
        self.message = msg
        # Go back, clear the line and write the message
        stdout.write("\r\033[K" + msg + "\n")

    def _update_progress(self, val):
        """Update bar's left to right progress and percentage.
        """
        # Calculate the rounded percentage
        new_percentage = round(val/self.total, 2)
        # Only if the "visible" percentages changed printing is necessary
        if new_percentage > self.percentage:
            self.percentage = new_percentage
            # Calculate number of characters to print
            print_chars = int(round(self.percentage * self.chars))
            # Build bar string
            bar_string = "=" * print_chars + \
                " " * (self.chars - print_chars)
            # Build percentage string
            percentage_string = "{0:.0f}%\r".format(new_percentage * 100) \
                                            .rjust(5)
            # Write bar and percentage strings
            stdout.write("\r[%s] %s" % (bar_string, percentage_string))

            # If the percentage is 1.0
            if new_percentage == 1.0:
                self.done = True
                stdout.write("\n")
