from sys import stdout
from .utilities import get_terminal_size


class Bar:
    """ Use this class to display progress.
    Make sure your command line interface understands ANSI escape codes.
    """

    bracket_characters = 2
    percentage_characters = 6

    def __init__(self, total, message=None, columns=None):
        """ Args:
            total (int): highest number representing 100%
            columns (Optional[int]): number of characters between brackets
            message (Optional[int]): initial message
        """
        self.total = total  # subtract 1 as most iterators go to n-1
        self.characters = self._calculate_characters(columns)
        self.value = 0
        self.percentage = 0
        # Print message if given, otherwise just an empty bar
        if message:
            self.message = self._clean_message(message)
            stdout.write(self.message + "\n")
        else:
            self.message = None
        # Print empty bar
        stdout.write("\r[%s]   0%%\n" % (" " * self.characters))

    def update(self, value=None):
        """ Pass either a string, a number or nothing as 'value'.
        If passed a string, update the displayed message.
        If passed a number, update progress and percentage.
        If passed nothing, increment progress by one.
        """
        # If 'value' is a str update the message above the bar
        if isinstance(value, str):
            self._update_message(value)
        # Otherwise update progress with value
        elif value:
            self._update_progress(value)
        # If no value is given, increment by one
        elif value is None:
            self._update_progress(self.value + 1)

    def clear(self):
        """Erase everything and move cursor to first position.
        """
        clear_string = "\r\033[F\033[K"  # Delete the line with the bar
        if self.message is not None:
            # Move up a line if a message was shown
            clear_string += "\033[F\033[K"
        stdout.write(clear_string)
        # Initialize state
        self.percentage = 0
        self.value = 0
        self.message = None

    def _calculate_characters(self, columns):
        if columns is None:
            columns = get_terminal_size()[0]
        return columns - self.bracket_characters - self.percentage_characters

    def _clean_message(self, msg):
        """Make sure the message has no new lines, and is not longer than
        'characters'.
        """
        msg = msg.replace("\n", "")
        if len(msg) > self.characters:
            msg = msg[:(self.characters - 3)] + "..."
        return msg

    def _update_message(self, msg):
        """Update message displayed above bar.
        """
        msg = self._clean_message(msg)
        if self.message:
            # If there was a message before go up an additional line
            stdout.write("\033[F")
        self.message = msg
        # Go back, clear the line and write the message
        stdout.write("\r\033[F\033[K%s\n\n" % msg)

    def _update_progress(self, val):
        """Update bar's left to right progress and percentage.
        """
        if self.total < val:
            val = self.total

        self.value = val
        new_percentage = round(val / self.total, 2)

        # Print only if the visible percentages changed (2 decimal places)
        if new_percentage > self.percentage:
            self.percentage = new_percentage
            # Write bar and percentage strings
            stdout.write("\033[F\r%s\n" % self.bottom_line_string())

    def bottom_line_string(self):
        progress_characters = int(round(self.percentage * self.characters))
        bar_string = "[" + "█" * progress_characters + \
                     " " * (self.characters - progress_characters) + "]"
        percentage_string = "{0:.0f}%\r".format(self.percentage * 100) \
            .rjust(self.percentage_characters)
        return bar_string + percentage_string
