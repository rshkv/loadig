from datetime import datetime
from sys import stdout
import shutil


class Bar:
    """ Use this class to display progress.
    Make sure your command line interface understands ANSI escape codes.
    """
    percentage_characters = 5
    time_characters = 11

    def __init__(self, total, message=None, columns=None):
        """ Args:
            total (int): highest number representing 100%
            columns (Optional[int]): number of characters in line
            message (Optional[int]): initial message
        """
        self.total = total  # subtract 1 as most iterators go to n-1
        self.characters = self._calculate_characters(columns)
        self.value = 0
        self.percentage = 0
        self.message = self._clean_message(message)
        if message:
            stdout.write(self.message + "\n")
        # Print empty bar
        stdout.write("\r%s   0%%\n" % (" " * self.characters))
        self.start_time = datetime.now()

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
        clear_string = "\r\033[F\033[K"  # Delete the bottom line
        if self.message is not None:
            # Move up a line if a message was shown
            clear_string += "\033[F\033[K"
        stdout.write(clear_string)
        # Initialize state
        self.percentage = 0
        self.value = 0
        self.message = None

    def _calculate_characters(self, columns):
        """Calculate number of characters to use for bar.
        """
        if columns is None:
            columns = shutil.get_terminal_size()[0]
        return (columns - self.percentage_characters -
                self.time_characters)

    def _clean_message(self, msg):
        """Cleans the message of new lines and slices to fit onto line.
        """
        if msg is None:
            return None
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
        """Update bar's left to right progress, percentage and time.
        """
        if self.total < val:
            val = self.total
        self.value = val
        self.percentage = round(val / self.total, 2)
        # Write bar and percentage strings
        stdout.write("\033[F\r%s\n" % self.bottom_line_string())

    def bottom_line_string(self):
        """Generate string to be printed as bottom line.
        Containing the bar itself, percentage of progress and expected time.
        """
        progress_characters = int(round(self.percentage * self.characters))
        bar_string = "█" * progress_characters + \
                     " " * (self.characters - progress_characters)
        percentage_string = "{0:.0f}%".format(self.percentage * 100) \
            .rjust(self.percentage_characters)
        time_string = self.wait_time().rjust(self.time_characters)
        return bar_string + percentage_string + time_string

    def wait_time(self):
        """Get time passed since initialization and approximate time to end.
        """
        if self.percentage < 0.01:
            return ""
        passed_time = datetime.now() - self.start_time
        expected_time = passed_time * (1 / self.percentage - 1)
        return str(expected_time).split('.')[0]
