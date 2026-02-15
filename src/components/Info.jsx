import Button from "@mui/material/Button";
import Dialog from "@mui/material/Dialog";
import DialogActions from "@mui/material/DialogActions";
import DialogContent from "@mui/material/DialogContent";
import DialogContentText from "@mui/material/DialogContentText";
import DialogTitle from "@mui/material/DialogTitle";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemText from "@mui/material/ListItemText";
import ListItemAvatar from "@mui/material/ListItemAvatar";
import Avatar from "@mui/material/Avatar";
import Typography from "@mui/material/Typography";

export default function Info({ open, handleClose }) {
  return (
    <div>
      <Dialog
        open={open}
        onClose={handleClose}
        aria-labelledby="alert-dialog-title"
        aria-describedby="alert-dialog-description"
      >
        <DialogTitle id="alert-dialog-title">Info</DialogTitle>
        <DialogContent>
          <DialogContentText id="alert-dialog-description">
            <Typography variant="h6" component="h3">
              This tool made possible by:
            </Typography>
            <List>
              <ListItem
                button
                onClick={() =>
                  (window.location.href = "https://github.com/theoriginalayaka")
                }
              >
                <ListItemAvatar>
                  <Avatar
                    alt="Ayaka"
                    src="https://avatars.githubusercontent.com/theoriginalayaka"
                  />
                </ListItemAvatar>
                <ListItemText
                  primary="Ayaka"
                  secondary="for the original idea"
                />
              </ListItem>
              <ListItem
                button
                onClick={() =>
                  (window.location.href = "https://gemini.google/overview/image-generation")
                }
              >
                <ListItemAvatar>
                  <Avatar
                    alt="Google Nano Banana Pro"
                    src="https://gemini.google/images/spark_4c.png"
                  />
                </ListItemAvatar>
                <ListItemText
                  primary="Google Nano Banana Pro"
                  secondary="for the sticker images"
                />
              </ListItem>
              <ListItem
                button
                onClick={() =>
                (window.location.href =
                  "https://github.com/pStrikeZ")
                }
              >
                <ListItemAvatar>
                  <Avatar
                    alt="pStrikeZ"
                    src="https://avatars.githubusercontent.com/pStrikeZ"
                  />
                </ListItemAvatar>
                <ListItemText
                  primary="pStrikeZ"
                  secondary="for ONGEKI version of the project"
                />
              </ListItem>
              <ListItem
                button
                onClick={() =>
                (window.location.href =
                  "https://github.com/pStrikeZ/ongeki-stickers/graphs/contributors")
                }
              >
                <ListItemAvatar>
                  <Avatar
                    alt="Contributors"
                    src="https://avatars.githubusercontent.com/u/583231"
                  />
                </ListItemAvatar>
                <ListItemText
                  primary="Contributors"
                  secondary="for the help with the code"
                />
              </ListItem>
            </List>
            <Typography variant="h6" component="h3">
              You can find the source code or contribute here:
            </Typography>
            <List>
              <ListItem
                button
                onClick={() =>
                (window.location.href =
                  "https://github.com/pStrikeZ/ongeki-stickers")
                }
              >
                <ListItemAvatar>
                  <Avatar
                    alt="GitHub"
                    src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"
                  />
                </ListItemAvatar>
                <ListItemText primary="GitHub" secondary="Source Code" />
              </ListItem>
            </List>
            {/*
            <Typography variant="h6" component="h3">
              The discord bot:
            </Typography>
            <List>
              <ListItem
                button
                onClick={() =>
                (window.location.href =
                  "http://link.ayaka.one/stbot")
                }
              >
                <ListItemAvatar>
                  <Avatar
                    alt="Discord"
                    src="https://cdn.discordapp.com/embed/avatars/0.png"
                  />
                </ListItemAvatar>
                <ListItemText
                  primary="Sekai Stickers"
                  secondary="Add more fun to your server."
                />
              </ListItem>
            </List>
            */}
            {/*             <Typography variant="h6" component="h3">
              Total stickers made using the app:
              <br />
              {config?.global
                ? config?.global.toLocaleString() + " Sticker"
                : "not available"}
            </Typography> */}
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose} color="secondary" autoFocus>
            Close
          </Button>
        </DialogActions>
      </Dialog>
    </div>
  );
}
