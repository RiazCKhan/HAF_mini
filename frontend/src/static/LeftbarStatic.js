import SupportAgentIcon from "@mui/icons-material/SupportAgent";
import Diversity3Icon from "@mui/icons-material/Diversity3";
import HandshakeIcon from "@mui/icons-material/Handshake";
import HealthAndSafetyIcon from "@mui/icons-material/HealthAndSafety";
import LocalShippingIcon from "@mui/icons-material/LocalShipping";

export const LeftBarStatic = [
  {
    id: 1,
    title: "Agent",
    icon: <SupportAgentIcon />,
    link: "/agents"
  },
  {
    id: 2,
    title: "Client",
    icon: < Diversity3Icon />,
    link: "/clients"
  },
  {
    id: 3,
    title: "Donor",
    icon: <HandshakeIcon />,
    link: "/donors"
  },
  {
    id: 4,
    title: "Donation",
    icon: <HealthAndSafetyIcon />,
    link: "/donations"
  },
  {
    id: 5,
    title: "Delivery",
    icon: <LocalShippingIcon />,
    link: "/deliveries"
  }
]